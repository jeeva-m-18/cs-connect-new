import sys, os
os.environ['PYTHONIOENCODING'] = 'utf-8'
sys.path.insert(0, r'c:\Users\LENOVO\Desktop\Mini project\cs_connect')
os.chdir(r'c:\Users\LENOVO\Desktop\Mini project\cs_connect')
from dotenv import load_dotenv
load_dotenv()
import psycopg2

conn = psycopg2.connect(os.environ.get('LOCAL_DATABASE_URL'))
cur = conn.cursor()

# Check website_content titles
cur.execute('SELECT title FROM website_content')
rows = cur.fetchall()
print('=== website_content titles ===')
for r in rows:
    print(r[0].encode('ascii', 'replace').decode())

# Check faculty table for HOD
print('\n=== faculty with HOD/Head designation ===')
cur.execute("SELECT name, designation, email FROM faculty WHERE designation ILIKE '%hod%' OR designation ILIKE '%head%' OR designation ILIKE '%professor%'")
rows = cur.fetchall()
for r in rows:
    print(r[0], '|', r[1], '|', r[2])

# All faculty
print('\n=== All faculty ===')
cur.execute("SELECT name, designation FROM faculty LIMIT 10")
rows = cur.fetchall()
for r in rows:
    print(r[0], '|', r[1])

# Total counts
cur.execute('SELECT COUNT(*) FROM faculty')
print('\nTotal faculty:', cur.fetchone()[0])
cur.execute('SELECT COUNT(*) FROM website_content')
print('Total website_content rows:', cur.fetchone()[0])

cur.close()
conn.close()
