import sys, os
os.environ['PYTHONIOENCODING'] = 'utf-8'
sys.path.insert(0, r'c:\Users\LENOVO\Desktop\Mini project\cs_connect')
os.chdir(r'c:\Users\LENOVO\Desktop\Mini project\cs_connect')
from dotenv import load_dotenv
load_dotenv()
import psycopg2

conn = psycopg2.connect(os.environ.get('LOCAL_DATABASE_URL'))
cur = conn.cursor()

def test_query(table_name, query, expected_cols_count):
    try:
        cur.execute(query)
        rows = cur.fetchall()
        print(f"[{table_name}] Query OK - Found {len(rows)} matching rows")
    except Exception as e:
        print(f"[{table_name}] ERROR: {e}")
        conn.rollback()

queries = {
    "faculty": "SELECT name, designation, research, email FROM faculty LIMIT 1;",
    "document_chunks": "SELECT document_name, content FROM document_chunks LIMIT 1;",
    "books": "SELECT title, author, category, availability::text FROM books LIMIT 1;",
    "alumni": "SELECT name, company, package FROM alumni LIMIT 1;",
    "timetable_subjects": "SELECT full_name, code, faculty_name FROM timetable_subjects LIMIT 1;",
    "website_content": "SELECT title, content FROM website_content LIMIT 1;"
}

print("=== Testing individual table queries for LLM Context ===")
for table, q in queries.items():
    test_query(table, q, 1)

print("\n=== Testing The Full LLM Query ===")
try:
    from llm_engine import fetch_ranked_context
    test_keywords = ["cse", "lab", "python", "ai", "jeswin", "library"]
    for kw in test_keywords:
        print(f"Searching context for: '{kw}'")
        res = fetch_ranked_context([kw])
        print(f" -> Found {len(res)} results")
        for idx, r in enumerate(res[:2]):
            print(f"    {idx+1}. [{r['category']}] {r['title'][:40]}")
except Exception as e:
    import traceback
    print(f"Error in full query test: {e}")
    traceback.print_exc()

cur.close()
conn.close()
