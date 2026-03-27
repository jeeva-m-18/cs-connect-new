import os
import sys
import json
from dotenv import load_dotenv

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import get_schema_summary, db_connection

def inspect():
    load_dotenv()
    schema = get_schema_summary()
    
    target_tables = ['issues', 'requests', 'library_fines']
    for table in target_tables:
        print(f"\n--- Table: {table} ---")
        cols = schema.get(table, "NOT FOUND")
        if isinstance(cols, list):
            for c in cols:
                print(f"  - {c}")
        else:
            print(f"  {cols}")

    with db_connection() as conn:
        with conn.cursor() as cur:
            # Check for issues_with_fines view definition
            cur.execute("SELECT view_definition FROM information_schema.views WHERE table_name = 'issues_with_fines'")
            view_def = cur.fetchone()
            if view_def:
                print("\n--- View Definition: issues_with_fines ---")
                print(view_def[0])

if __name__ == "__main__":
    inspect()
