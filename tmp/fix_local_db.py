"""
Fixes the local csconnect DB to add missing PRIMARY KEY constraints,
UNIQUE constraints, and repair SERIAL sequences so INSERT/UPDATE works correctly.
Run: python tmp/fix_local_db.py
"""
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname='csconnect', user='postgres', password='@mugdham', host='127.0.0.1')
conn.autocommit = True
cur = conn.cursor()

fixes = [
    # Primary keys
    "ALTER TABLE news_ticker ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE alumni ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE faculty ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE users ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE books ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE issues ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE semesters ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE notices ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE notifications ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE timetable ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE timetable_subjects ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE timetable_meta ADD PRIMARY KEY (batch)",
    "ALTER TABLE home_stats ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE internal_marks ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE internships ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE mous ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE programs ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE requests ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE results ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE resource_downloads ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE placement_batches ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE placement_companies ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE placement_drives ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE placement_summary ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE placement_applications ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE library_fines ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE library_loans ADD PRIMARY KEY (id)",
    "ALTER TABLE library_notifications ADD PRIMARY KEY (id)",
    "ALTER TABLE book_requests ADD PRIMARY KEY (id)",
    "ALTER TABLE book_reservations ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE events ADD PRIMARY KEY (sl_no)",
    "ALTER TABLE document_chunks ADD PRIMARY KEY (id)",
    "ALTER TABLE website_content ADD PRIMARY KEY (id)",
    "ALTER TABLE portal_sessions ADD PRIMARY KEY (id)",
    "ALTER TABLE settings ADD PRIMARY KEY (id)",
    "ALTER TABLE resources ADD PRIMARY KEY (id)",
    "ALTER TABLE assignments ADD PRIMARY KEY (id)",
    "ALTER TABLE submissions ADD PRIMARY KEY (id)",
    "ALTER TABLE student_semester_gpas ADD PRIMARY KEY (id)",
    "ALTER TABLE student_subject_marks ADD PRIMARY KEY (id)",
    "ALTER TABLE student_performance ADD PRIMARY KEY (user_id)",
    "ALTER TABLE site_data ADD PRIMARY KEY (key)",

    # UNIQUE constraints
    "ALTER TABLE users ADD CONSTRAINT users_email_unique UNIQUE (email)",
    "ALTER TABLE users ADD CONSTRAINT users_userid_unique UNIQUE (user_id)",
    "ALTER TABLE document_chunks ADD CONSTRAINT doc_chunks_unique UNIQUE (document_name, chunk_index)",

    # SERIAL sequences for auto-increment
    "CREATE SEQUENCE IF NOT EXISTS news_ticker_sl_no_seq; ALTER TABLE news_ticker ALTER COLUMN sl_no SET DEFAULT nextval('news_ticker_sl_no_seq')",
    "CREATE SEQUENCE IF NOT EXISTS alumni_sl_no_seq; ALTER TABLE alumni ALTER COLUMN sl_no SET DEFAULT nextval('alumni_sl_no_seq')",
    "CREATE SEQUENCE IF NOT EXISTS faculty_sl_no_seq; ALTER TABLE faculty ALTER COLUMN sl_no SET DEFAULT nextval('faculty_sl_no_seq')",
    "CREATE SEQUENCE IF NOT EXISTS users_sl_no_seq; ALTER TABLE users ALTER COLUMN sl_no SET DEFAULT nextval('users_sl_no_seq')",
    "CREATE SEQUENCE IF NOT EXISTS books_sl_no_seq; ALTER TABLE books ALTER COLUMN sl_no SET DEFAULT nextval('books_sl_no_seq')",
    "CREATE SEQUENCE IF NOT EXISTS issues_sl_no_seq; ALTER TABLE issues ALTER COLUMN sl_no SET DEFAULT nextval('issues_sl_no_seq')",
    "CREATE SEQUENCE IF NOT EXISTS semesters_sl_no_seq; ALTER TABLE semesters ALTER COLUMN sl_no SET DEFAULT nextval('semesters_sl_no_seq')",
    "CREATE SEQUENCE IF NOT EXISTS library_fines_sl_no_seq; ALTER TABLE library_fines ALTER COLUMN sl_no SET DEFAULT nextval('library_fines_sl_no_seq')",
    "CREATE SEQUENCE IF NOT EXISTS library_loans_id_seq; ALTER TABLE library_loans ALTER COLUMN id SET DEFAULT nextval('library_loans_id_seq')",
    "CREATE SEQUENCE IF NOT EXISTS library_notifications_id_seq; ALTER TABLE library_notifications ALTER COLUMN id SET DEFAULT nextval('library_notifications_id_seq')",
    "CREATE SEQUENCE IF NOT EXISTS book_requests_id_seq; ALTER TABLE book_requests ALTER COLUMN id SET DEFAULT nextval('book_requests_id_seq')",
]

ok = 0
for sql in fixes:
    try:
        cur.execute(sql)
        ok += 1
    except Exception as e:
        print(f"SKIP ({e.__class__.__name__}): {sql[:60]}...")

conn.close()
print(f"\nDone. {ok}/{len(fixes)} fixes applied.")
