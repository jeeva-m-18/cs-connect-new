import sys
import os
from dotenv import load_dotenv

load_dotenv()
from database import get_db_connection

conn = get_db_connection()
cur = conn.cursor()

query_string = "s6 cse monday"
patterns = ['%s6%', '%cse%', '%monday%']

query = """
    SELECT 'TIMETABLE' as category, t.day || ' Period ' || t.period as title, 
           'Batch: ' || t.batch || ' | Subject: ' || COALESCE(ts.full_name, t.subject_code) as details,
           'Faculty: ' || COALESCE(ts.faculty_name, t.faculty_code) as extra,
           similarity(t.batch || ' ' || t.day::text, %s::text) as score
    FROM timetable t
    LEFT JOIN timetable_subjects ts ON t.subject_code = ts.code AND t.batch = ts.batch
    WHERE t.batch ILIKE ANY(%s) OR t.day ILIKE ANY(%s) OR ts.full_name ILIKE ANY(%s)
    ORDER BY score DESC LIMIT 10
"""

cur.execute(query, [query_string, patterns, patterns, patterns])
rows = cur.fetchall()
for r in rows:
    print(r)
