"""
Comprehensive test of the local csconnect database.
Tests: connection, all key tables, row counts, INSERT/DELETE, sequences.
"""
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname='csconnect', user='postgres', password='@mugdham', host='127.0.0.1')
conn.autocommit = False
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

print("=" * 50)
print("LOCAL DATABASE HEALTH CHECK")
print("=" * 50)

# 1. Connection
cur.execute("SELECT current_database(), version()")
row = cur.fetchone()
print(f"\n[OK] Connected to: {row[0]}")
print(f"     PostgreSQL: {row[1][:40]}...")

# 2. Row counts for all key tables
key_tables = [
    'users', 'faculty', 'books', 'issues', 'semesters',
    'notifications', 'timetable', 'notices', 'requests',
    'library_fines', 'document_chunks', 'website_content'
]
print("\n[TABLE ROW COUNTS]")
all_ok = True
for tbl in key_tables:
    try:
        cur.execute(f"SELECT COUNT(*) FROM {tbl}")
        count = cur.fetchone()[0]
        print(f"  {tbl:<25} {count} rows")
    except Exception as e:
        print(f"  {tbl:<25} ERROR: {e}")
        all_ok = False

# 3. Test INSERT + sequence + DELETE (using notifications as test table)
print("\n[INSERT / SEQUENCE TEST]")
try:
    cur.execute(
        "INSERT INTO notifications (user_id, title, body, category) VALUES (%s,%s,%s,%s) RETURNING sl_no",
        ('TEST_USER', 'Test Notification', 'Health check', 'system')
    )
    new_id = cur.fetchone()[0]
    print(f"  INSERT OK  -> new sl_no = {new_id}")
    cur.execute("DELETE FROM notifications WHERE sl_no = %s", (new_id,))
    print(f"  DELETE OK  -> cleaned up")
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"  FAILED: {e}")
    all_ok = False

# 4. Users check
print("\n[USERS]")
cur.execute("SELECT user_id, email, role FROM users ORDER BY sl_no")
for r in cur.fetchall():
    print(f"  {r['role']:<10} {r['user_id']:<15} {r['email']}")

# 5. Semesters/notes check
print("\n[NOTES CHECK - first 3 subjects with notes]")
import json
cur.execute("SELECT subjects FROM semesters")
found = 0
for row in cur.fetchall():
    subjects = json.loads(row['subjects']) if isinstance(row['subjects'], str) else row['subjects']
    for subj in subjects:
        notes = subj.get('notes', {})
        if isinstance(notes, dict) and notes:
            print(f"  {subj['name']}: {list(notes.keys())}")
            found += 1
            if found >= 3:
                break
    if found >= 3:
        break
if found == 0:
    print("  No subjects with notes found yet (expected if no uploads done)")

conn.close()

print("\n" + "=" * 50)
print("RESULT:", "ALL SYSTEMS OK" if all_ok else "SOME ISSUES FOUND")
print("=" * 50)
