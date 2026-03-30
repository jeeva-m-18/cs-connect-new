"""
Comprehensive audit of all potential issues in the local DB after migration.
"""
import psycopg2
import psycopg2.extras
import json

conn = psycopg2.connect(dbname='csconnect', user='postgres', password='@mugdham', host='127.0.0.1')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

print("=== 1. news_ticker columns ===")
cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='news_ticker'")
print([r[0] for r in cur.fetchall()])

print("\n=== 2. notes format in semesters ===")
cur.execute("SELECT sl_no, title, subjects FROM semesters")
for row in cur.fetchall():
    subjects = json.loads(row['subjects']) if isinstance(row['subjects'], str) else row['subjects']
    for subj in subjects:
        notes = subj.get('notes')
        if notes:
            note_type = type(notes).__name__
            print(f"  sem={row['sl_no']} subj={subj.get('name','')} notes_type={note_type}: {str(notes)[:80]}")

print("\n=== 3. users table check ===")
cur.execute("SELECT sl_no, user_id, email, role FROM users")
for r in cur.fetchall():
    print(f"  {dict(r)}")

print("\n=== 4. Missing PKs ===")
cur.execute("""
    SELECT table_name FROM information_schema.tables t
    WHERE table_schema='public' AND table_type='BASE TABLE'
    AND NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints tc
        WHERE tc.table_name = t.table_name
        AND tc.constraint_type = 'PRIMARY KEY'
        AND tc.table_schema = 'public'
    )
""")
missing_pk = [r[0] for r in cur.fetchall()]
print("Tables with no PK:", missing_pk)

print("\n=== 5. Sequences check ===")
cur.execute("SELECT sequence_name, last_value FROM information_schema.sequences s JOIN pg_sequences ps ON ps.sequencename = s.sequence_name WHERE s.sequence_schema='public'")
for r in cur.fetchall():
    print(f"  {r['sequence_name']}: last_value={r['last_value']}")

conn.close()
