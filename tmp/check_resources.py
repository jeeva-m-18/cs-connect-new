import sys
import os
from dotenv import load_dotenv

load_dotenv()
from database import get_db_connection

conn = get_db_connection()
cur = conn.cursor()

try:
    cur.execute("SELECT title, category, semester FROM resources WHERE category = 'syllabus'")
    rows = cur.fetchall()
    if not rows:
        print("No syllabus records found.")
    else:
        for r in rows:
            print(f"Syllabus found: {r[0]} (Sem {r[2]})")
except Exception as e:
    print(f"Error querying resources table: {e}")
finally:
    conn.close()
