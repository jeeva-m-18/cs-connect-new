import os
import sys
import json
from dotenv import load_dotenv

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import db_connection

def check():
    load_dotenv()
    with db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT table_name, column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name IN ('issues', 'requests', 'library_fines', 'users')
                AND table_schema = 'public'
                ORDER BY table_name, ordinal_position
            """)
            cols = cur.fetchall()
            print(json.dumps([list(c) for c in cols], indent=2))

if __name__ == "__main__":
    check()
