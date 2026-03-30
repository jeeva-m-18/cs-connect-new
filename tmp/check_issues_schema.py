import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def get_table_schema(url, table_name):
    try:
        conn = psycopg2.connect(url)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            query = """
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = %s 
            ORDER BY ordinal_position;
            """
            cur.execute(query, (table_name,))
            return cur.fetchall()
    except Exception as e:
        return f"Error: {e}"

local_url = os.environ.get("LOCAL_DATABASE_URL")
neon_url = os.environ.get("NEON_DATABASE_URL")

print(f"--- Schema for table 'issues' ---")
print(f"LOCAL: {get_table_schema(local_url, 'issues')}")
print(f"NEON : {get_table_schema(neon_url, 'issues')}")

print(f"\n--- Schema for table 'issues_with_fines' ---")
print(f"LOCAL: {get_table_schema(local_url, 'issues_with_fines')}")
print(f"NEON : {get_table_schema(neon_url, 'issues_with_fines')}")
