"""
Enable pg_trgm extension and test similarity() works.
"""
import sys, os
os.environ['PYTHONIOENCODING'] = 'utf-8'
sys.path.insert(0, r'c:\Users\LENOVO\Desktop\Mini project\cs_connect')
os.chdir(r'c:\Users\LENOVO\Desktop\Mini project\cs_connect')
from dotenv import load_dotenv
load_dotenv()
import psycopg2

conn = psycopg2.connect(os.environ.get('LOCAL_DATABASE_URL'))
conn.autocommit = True
cur = conn.cursor()

print("Enabling pg_trgm extension...")
cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")
print("pg_trgm enabled!")

# Test it works
cur.execute("SELECT similarity('hod', 'HoD & Asso. Professor')")
result = cur.fetchone()[0]
print(f"similarity('hod', 'HoD & Asso. Professor') = {result}")

cur.execute("SELECT similarity('hod'::text, 'jeswin'::text)")
result = cur.fetchone()[0]
print(f"similarity('hod', 'jeswin') = {result}")

# Test the full faculty query
print("\n=== Testing full chatbot search for 'hod' ===")
patterns = ['%hod%', '%head%']
query_string = 'hod'
cur.execute("""
    SELECT 'FACULTY' as cat, name as title, 
           designation,
           GREATEST(similarity(name::text, %s::text), similarity(designation::text, %s::text), 0.15) as score
    FROM faculty 
    WHERE name ILIKE ANY(%s) OR designation ILIKE ANY(%s)
    ORDER BY score DESC
    LIMIT 5
""", (query_string, query_string, patterns, patterns))
rows = cur.fetchall()
print(f"Faculty results: {len(rows)}")
for r in rows:
    print(f"  {r[1]} | {r[2]} | score={r[3]:.3f}")

# Test website_content
print("\n=== Testing website_content search for 'hod' ===")
cur.execute("""
    SELECT title, GREATEST(similarity(title::text, %s::text), 0.15) as score
    FROM website_content
    WHERE title ILIKE ANY(%s) OR content ILIKE ANY(%s)
    ORDER BY score DESC
    LIMIT 5
""", (query_string, ['%hod%', '%principal%', '%head of department%'], ['%hod%', '%head of department%', '%jeswin%']))
rows = cur.fetchall()
print(f"Info results: {len(rows)}")
for r in rows:
    print(f"  {r[0][:60]} | score={r[1]:.3f}")

cur.close()
conn.close()
print("\nDone!")
