import sys
import os
from dotenv import load_dotenv

load_dotenv()
from database import get_db_connection

conn = get_db_connection()
cur = conn.cursor()
cur.execute("SELECT DISTINCT batch FROM timetable")
rows = cur.fetchall()
print("Batches in timetable:", [r[0] for r in rows])
