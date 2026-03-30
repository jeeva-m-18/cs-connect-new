import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

load_dotenv()

def check_deployment_ready(target_url):
    try:
        conn = psycopg2.connect(target_url)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            # 1. Check if all critical tables exist
            critical_tables = ["users", "books", "issues", "issues_with_fines"]
            cur.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public';
            """)
            existing_tables = [row['table_name'] for row in cur.fetchall()]
            
            missing = [t for t in critical_tables if t not in existing_tables]
            if missing:
                logger.error(f"Missing critical tables: {missing}")
                return False
            else:
                logger.info(f"Verified {len(existing_tables)} tables in Neon.")

            # 2. Check the controversial View: issues_with_fines (cause of crash)
            # The app expects: sl_no, book_id, user_id, issue_date, due_date, return_date, status, 
            # payment_requested_date, payment_status, renewal_count, effective_date, days_overdue, fine_amount
            cur.execute("""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = 'issues_with_fines'
            """)
            cols = {row['column_name']: row['data_type'] for row in cur.fetchall()}
            
            # Key check for "effective_date" (Local uses this, old Neon used "effective_end_date")
            if 'effective_date' not in cols:
                logger.error("CRITICAL: 'issues_with_fines' view is missing 'effective_date' column. This will cause crashes!")
                return False
            else:
                logger.info("View 'issues_with_fines' successfully verified with 'effective_date' column.")

            # 3. Check for sl_no column (Serial handling)
            if cols.get('sl_no') != 'integer':
                logger.error(f"Column 'sl_no' in issues must be integer/serial. Found: {cols.get('sl_no')}")
                return False
            
            logger.info("All deployment checks PASSED! This database is safe for Render.")
            return True

    except Exception as e:
        logger.error(f"Connectivity error to Neon: {e}")
        return False
    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("NEON_DATABASE_URL")
    if not url:
        logger.error("No database URL provided.")
        sys.exit(1)
        
    if check_deployment_ready(url):
        logger.info("Database is clean and ready for deployment.")
    else:
        logger.error("Ready check FAILED. Please sync with Local before deploying.")
        sys.exit(1)
