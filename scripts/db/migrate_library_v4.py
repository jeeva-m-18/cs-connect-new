import os
import sys
import psycopg2
from dotenv import load_dotenv

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from database import db_connection

def migrate():
    load_dotenv()
    
    try:
        with db_connection() as conn:
            with conn.cursor() as cur:
                print("Starting Migration v4: Standardizing library system...")

                # 1. Drop dependent views first
                print("Dropping dependent views...")
                cur.execute("DROP VIEW IF EXISTS issues_with_fines")

                # 2. Standardize Timestamps (Convert to timestamptz)
                print("Converting timestamps to timestamptz (UTC)...")
                tables_to_update = {
                    'issues': ['issue_date', 'due_date', 'return_date', 'payment_requested_date'],
                    'requests': ['request_date'],
                    'library_fines': ['created_at'],
                    'users': ['created_at']
                }
                for table, cols in tables_to_update.items():
                    print(f"  Refactoring table: {table}")
                    for col in cols:
                        # Assuming existing data was UTC-based
                        cur.execute(f"ALTER TABLE {table} ALTER COLUMN {col} TYPE timestamptz USING {col} AT TIME ZONE 'UTC'")

                # 3. Add Request Date Columns to issues
                print("Adding request date tracking columns to issues...")
                cur.execute("ALTER TABLE issues ADD COLUMN IF NOT EXISTS return_request_date timestamptz")
                cur.execute("ALTER TABLE issues ADD COLUMN IF NOT EXISTS renew_request_date timestamptz")

                # 4. Standardize Table Structure
                print("Standardizing library_fines table...")
                # Rename student_id to user_id for consistency
                cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='library_fines' AND column_name='student_id'")
                if cur.fetchone():
                    cur.execute("ALTER TABLE library_fines RENAME COLUMN student_id TO user_id")
                
                # Drop redundant loan_id if issue_id exists
                cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='library_fines' AND column_name='loan_id'")
                if cur.fetchone():
                    cur.execute("ALTER TABLE library_fines DROP COLUMN loan_id")

                # 5. Recreate Fine Calculation View
                print("Recreating issues_with_fines view...")
                
                # Logic: Fine is ₹1 per day. Stops at the MIN of (return_request_date, renew_request_date, return_date).
                view_sql = """
                CREATE OR REPLACE VIEW issues_with_fines AS 
                SELECT 
                    i.*,
                    COALESCE(
                        LEAST(
                            COALESCE(return_request_date, '9999-12-31'::timestamptz),
                            COALESCE(renew_request_date, '9999-12-31'::timestamptz),
                            COALESCE(return_date, '9999-12-31'::timestamptz),
                            CURRENT_TIMESTAMP AT TIME ZONE 'UTC'
                        ),
                        CURRENT_TIMESTAMP AT TIME ZONE 'UTC'
                    ) AS effective_end_date,
                    GREATEST(0, (
                        DATE_PART('day', (
                            COALESCE(
                                LEAST(
                                    COALESCE(return_request_date, '9999-12-31'::timestamptz),
                                    COALESCE(renew_request_date, '9999-12-31'::timestamptz),
                                    COALESCE(return_date, '9999-12-31'::timestamptz),
                                    CURRENT_TIMESTAMP AT TIME ZONE 'UTC'
                                ),
                                CURRENT_TIMESTAMP AT TIME ZONE 'UTC'
                            ) - i.due_date
                        ))
                    ))::integer AS days_overdue,
                    GREATEST(0, (
                        DATE_PART('day', (
                            COALESCE(
                                LEAST(
                                    COALESCE(return_request_date, '9999-12-31'::timestamptz),
                                    COALESCE(renew_request_date, '9999-12-31'::timestamptz),
                                    COALESCE(return_date, '9999-12-31'::timestamptz),
                                    CURRENT_TIMESTAMP AT TIME ZONE 'UTC'
                                ),
                                CURRENT_TIMESTAMP AT TIME ZONE 'UTC'
                            ) - i.due_date
                        ))
                    ))::numeric * 1.00 AS fine_amount
                FROM issues i;
                """
                cur.execute(view_sql)

                conn.commit()
                print("Migration Successful!")

    except Exception as e:
        print(f"Migration Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    migrate()
