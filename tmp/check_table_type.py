import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def check_if_view(url, table_name):
    try:
        conn = psycopg2.connect(url)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            query = """
            SELECT table_type 
            FROM information_schema.tables 
            WHERE table_name = %s;
            """
            cur.execute(query, (table_name,))
            row = cur.fetchone()
            return row['table_type'] if row else "NOT FOUND"
    except Exception as e:
        return f"Error: {e}"

local_url = os.environ.get("LOCAL_DATABASE_URL")
neon_url = os.environ.get("NEON_DATABASE_URL")

print(f"--- Table Type for 'issues_with_fines' ---")
print(f"LOCAL: {check_if_view(local_url, 'issues_with_fines')}")
print(f"NEON : {check_if_view(neon_url, 'issues_with_fines')}")
