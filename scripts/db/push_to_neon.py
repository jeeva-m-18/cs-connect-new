import os
import subprocess
import logging
import sys
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

load_dotenv()

def push_to_neon(target_url):
    local_url = os.environ.get("LOCAL_DATABASE_URL")
    if not local_url:
        logger.error("LOCAL_DATABASE_URL not found in .env")
        return False

    logger.info("Starting fresh migration from Local to Neon...")
    
    # 1. Verification: Check if tools are available
    try:
        subprocess.run(["pg_dump", "--version"], check=True, capture_output=True)
        subprocess.run(["psql", "--version"], check=True, capture_output=True)
    except Exception:
        logger.error("PostgreSQL CLI tools (pg_dump, psql) are not installed or in PATH.")
        return False

    # 2. Dump Local Database
    dump_file = "local_dump.sql"
    logger.info(f"Dumping local database to {dump_file}...")
    try:
        # Use --no-owner and --no-privileges to avoid permission issues on Neon
        subprocess.run([
            "pg_dump", 
            "--no-owner", 
            "--no-privileges", 
            "--clean", 
            "--if-exists",
            "--dbname", local_url, 
            "--file", dump_file
        ], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to dump local database: {e}")
        return False

    # 3. Restore to Neon
    logger.info("Restoring dump to Neon (this may take a minute)...")
    try:
        # Use psql to execute the dump file on the target Neon URL
        subprocess.run([
            "psql", 
            "--dbname", target_url, 
            "--file", dump_file
        ], check=True)
        logger.info("Migration successful! Neon is now 100% in sync with Local.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to restore to Neon: {e}")
        return False
    finally:
        if os.path.exists(dump_file):
            os.remove(dump_file)
            logger.info("Temporary dump file removed.")

    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python push_to_neon.py <NEON_DATABASE_URL>")
        sys.exit(1)
    
    target = sys.argv[1]
    success = push_to_neon(target)
    if not success:
        sys.exit(1)
