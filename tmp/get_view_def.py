import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def get_view_definition(url, table_name):
    try:
        conn = psycopg2.connect(url)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            query = """
            SELECT view_definition 
            FROM information_schema.views 
            WHERE table_name = %s;
            """
            cur.execute(query, (table_name,))
            row = cur.fetchone()
            return row['view_definition'] if row else "NOT FOUND"
    except Exception as e:
        return f"Error: {e}"

local_url = os.environ.get("LOCAL_DATABASE_URL")
neon_url = os.environ.get("NEON_DATABASE_URL")

print(f"--- View Definition for 'issues_with_fines' ---")
print(f"LOCAL: {get_view_definition(local_url, 'issues_with_fines')}")
print(f"NEON : {get_view_definition(neon_url, 'issues_with_fines')}")
