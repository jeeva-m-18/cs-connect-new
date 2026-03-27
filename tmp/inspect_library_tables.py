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
    
    target_tables = ['issues', 'requests', 'library_fines', 'books', 'users']
    relevant_schema = {t: schema.get(t, "NOT FOUND") for t in target_tables}
    
    print("--- Schema Summary ---")
    print(json.dumps(relevant_schema, indent=2))
    
    with db_connection() as conn:
        with conn.cursor() as cur:
            # Check for views as well
            cur.execute("SELECT table_name FROM information_schema.views WHERE table_schema = 'public'")
            views = cur.fetchall()
            print("\n--- Views ---")
            print([v[0] for v in views])
            
            # Check for 'issues_with_fines' specifically
            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'issues_with_fines')")
            exists = cur.fetchone()[0]
            print(f"\nTable/View 'issues_with_fines' exists: {exists}")

if __name__ == "__main__":
    inspect()
