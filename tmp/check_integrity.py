import os
import sys
from dotenv import load_dotenv

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import db_connection

def check():
    load_dotenv()
    with db_connection() as conn:
        with conn.cursor() as cur:
            # 1. Orphaned books in issues
            cur.execute("""
                SELECT i.sl_no, i.book_id 
                FROM issues i 
                LEFT JOIN books b ON i.book_id = b.sl_no 
                WHERE b.sl_no IS NULL
            """)
            orphaned_books = cur.fetchall()
            print(f"Orphaned books in issues: {len(orphaned_books)}")
            for o in orphaned_books: print(o)

            # 2. Orphaned users in issues
            cur.execute("""
                SELECT i.sl_no, i.user_id 
                FROM issues i 
                LEFT JOIN users u ON i.user_id = u.user_id 
                WHERE u.user_id IS NULL
            """)
            orphaned_users = cur.fetchall()
            print(f"Orphaned users in issues: {len(orphaned_users)}")
            for o in orphaned_users: print(o)

            # 3. Active issues for same book/user
            cur.execute("""
                SELECT book_id, user_id, COUNT(*) 
                FROM issues 
                WHERE status = 'issued'
                GROUP BY book_id, user_id 
                HAVING COUNT(*) > 1
            """)
            duplicates = cur.fetchall()
            print(f"Duplicate active issues: {len(duplicates)}")
            for d in duplicates: print(d)
            
            # 4. Books that are 'issued' but also marked 'available'
            cur.execute("""
                SELECT b.sl_no, b.title 
                FROM books b
                JOIN issues i ON b.sl_no = i.book_id
                WHERE i.status = 'issued' AND b.availability = TRUE
            """)
            availability_mismatch = cur.fetchall()
            print(f"Books marked available while issued: {len(availability_mismatch)}")
            for m in availability_mismatch: print(m)

if __name__ == "__main__":
    check()
