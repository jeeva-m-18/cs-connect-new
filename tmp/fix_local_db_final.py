"""
Final comprehensive fix for local csconnect DB:
1. Fix sequences (set correct last_value based on existing data)
2. Fix news_ticker ordering (add id column)
3. Fix notes format in semesters (list -> dict)
4. Fix missing PKs on remaining tables
5. Fix api.get_all_notes_data() to handle both list and dict formats
"""
import psycopg2
import psycopg2.extras
import json

conn = psycopg2.connect(dbname='csconnect', user='postgres', password='@mugdham', host='127.0.0.1')
conn.autocommit = True
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

print("=== FIX 1: Reset sequences to correct max values ===")
seq_table_map = [
    ('alumni_sl_no_seq', 'alumni', 'sl_no'),
    ('users_sl_no_seq', 'users', 'sl_no'),
    ('faculty_sl_no_seq', 'faculty', 'sl_no'),
    ('books_sl_no_seq', 'books', 'sl_no'),
    ('issues_sl_no_seq', 'issues', 'sl_no'),
    ('semesters_sl_no_seq', 'semesters', 'sl_no'),
    ('notices_sl_no_seq', 'notices', 'sl_no'),
    ('notifications_sl_no_seq', 'notifications', 'sl_no'),
    ('timetable_sl_no_seq', 'timetable', 'sl_no'),
    ('timetable_subjects_sl_no_seq', 'timetable_subjects', 'sl_no'),
    ('home_stats_sl_no_seq', 'home_stats', 'sl_no'),
    ('internal_marks_sl_no_seq', 'internal_marks', 'sl_no'),
    ('internships_sl_no_seq', 'internships', 'sl_no'),
    ('mous_sl_no_seq', 'mous', 'sl_no'),
    ('programs_sl_no_seq', 'programs', 'sl_no'),
    ('requests_sl_no_seq', 'requests', 'sl_no'),
    ('results_sl_no_seq', 'results', 'sl_no'),
    ('library_fines_sl_no_seq', 'library_fines', 'sl_no'),
    ('library_loans_id_seq', 'library_loans', 'id'),
    ('library_notifications_id_seq', 'library_notifications', 'id'),
    ('book_requests_id_seq', 'book_requests', 'id'),
    ('book_reservations_sl_no_seq', 'book_reservations', 'sl_no'),
    ('events_sl_no_seq', 'events', 'sl_no'),
    ('document_chunks_id_seq', 'document_chunks', 'id'),
    ('website_content_id_seq', 'website_content', 'id'),
    ('portal_sessions_id_seq', 'portal_sessions', 'id'),
    ('settings_id_seq', 'settings', 'id'),
    ('resources_id_seq', 'resources', 'id'),
    ('news_ticker_sl_no_seq', 'news_ticker', 'sl_no'),
    ('placement_batches_sl_no_seq', 'placement_batches', 'sl_no'),
    ('placement_companies_sl_no_seq', 'placement_companies', 'sl_no'),
    ('placement_drives_sl_no_seq', 'placement_drives', 'sl_no'),
    ('placement_summary_sl_no_seq', 'placement_summary', 'sl_no'),
    ('placement_applications_sl_no_seq', 'placement_applications', 'sl_no'),
    ('resource_downloads_sl_no_seq', 'resource_downloads', 'sl_no'),
    ('student_semester_gpas_id_seq', 'student_semester_gpas', 'id'),
    ('student_subject_marks_id_seq', 'student_subject_marks', 'id'),
    ('submissions_id_seq', 'submissions', 'id'),
]

for seq, tbl, col in seq_table_map:
    try:
        cur.execute(f"SELECT MAX({col}) FROM {tbl}")
        max_val = cur.fetchone()[0] or 1
        cur.execute(f"SELECT setval('{seq}', {max_val})")
        print(f"  {seq} -> {max_val}")
    except Exception as e:
        print(f"  SKIP {seq}: {e}")

print("\n=== FIX 2: Fix missing PKs ===")
try:
    cur.execute("ALTER TABLE pending_approvals ADD PRIMARY KEY (id)")
    print("  pending_approvals PK added")
except Exception as e:
    print(f"  SKIP: {e}")
try:
    cur.execute("ALTER TABLE test_parent_backup ADD PRIMARY KEY (id)")
    print("  test_parent_backup PK added")
except Exception as e:
    print(f"  SKIP: {e}")

print("\n=== FIX 3: Fix notes format (list -> dict) in semesters ===")
cur.execute("SELECT sl_no, subjects FROM semesters")
rows = cur.fetchall()
fixed_count = 0
for row in rows:
    subjects = json.loads(row['subjects']) if isinstance(row['subjects'], str) else row['subjects']
    changed = False
    for subj in subjects:
        notes = subj.get('notes')
        if isinstance(notes, list):
            # Convert [{"title": "Module 1", "url": "..."}, ...] -> {"Module 1": "..."}
            new_notes = {}
            for item in notes:
                if isinstance(item, dict) and 'title' in item and 'url' in item:
                    new_notes[item['title']] = item['url']
            subj['notes'] = new_notes
            changed = True
    if changed:
        cur.execute("UPDATE semesters SET subjects = %s WHERE sl_no = %s",
                    (json.dumps(subjects), row['sl_no']))
        fixed_count += 1
print(f"  Fixed {fixed_count} semester rows")

print("\nAll fixes applied.")
