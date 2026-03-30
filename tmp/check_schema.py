"""
Fix chatbot issues: seed institutional leadership data into website_content
"""
import sys, os
os.environ['PYTHONIOENCODING'] = 'utf-8'
sys.path.insert(0, r'c:\Users\LENOVO\Desktop\Mini project\cs_connect')
os.chdir(r'c:\Users\LENOVO\Desktop\Mini project\cs_connect')
from dotenv import load_dotenv
load_dotenv()
import psycopg2

conn = psycopg2.connect(os.environ.get('LOCAL_DATABASE_URL'))
cur = conn.cursor()

# Check the schema of website_content
cur.execute("""
    SELECT column_name, data_type, is_nullable, column_default
    FROM information_schema.columns
    WHERE table_name = 'website_content'
    ORDER BY ordinal_position
""")
cols = cur.fetchall()
print("=== website_content schema ===")
for c in cols:
    print(f"  {c[0]} | {c[1]} | nullable={c[2]} | default={c[3]}")

# Also sample a row to see what url looks like
cur.execute("SELECT id, url, title, LEFT(content, 100) FROM website_content LIMIT 3")
rows = cur.fetchall()
print("\n=== Sample rows ===")
for r in rows:
    print(f"  id={r[0]}, url={r[1]}, title={r[2]}")

cur.close()
conn.close()
