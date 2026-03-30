from database import db_connection
import pypdf

# Check if tables exist
try:
    with db_connection() as conn:
        print('Checking DB...')
        row = conn.execute("SELECT COUNT(*) FROM document_chunks").fetchone()
        print('Current chunks count:', row['count'])
except Exception as e:
    print("Error:", e)
