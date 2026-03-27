import os
import sys
import json
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import db_connection
from models.issue import Issue
from models.request import Request

def setup_test_data():
    load_dotenv()
    with db_connection() as conn:
        with conn.cursor() as cur:
            # Clean up
            cur.execute("DELETE FROM requests WHERE requested_by LIKE 'test_user_%'")
            cur.execute("DELETE FROM issues WHERE user_id LIKE 'test_user_%'")
            cur.execute("DELETE FROM users WHERE user_id LIKE 'test_user_%'")
            
            # Create test users
            cur.execute("INSERT INTO users (name, user_id, email, role, status) VALUES ('Test Student 1', 'test_user_1', 'test1@example.com', 'student', 'Active')")
            cur.execute("INSERT INTO users (name, user_id, email, role, status) VALUES ('Test Student 2', 'test_user_2', 'test2@example.com', 'student', 'Active')")
            
            # Use an existing book for tests (sl_no 1)
            cur.execute("SELECT sl_no FROM books LIMIT 1")
            book_id = cur.fetchone()[0]
            
            conn.commit()
            return book_id

def test_scenario_1(book_id):
    print("\n--- Scenario 1: Fine stops at request date ---")
    # 1. Create issue with due date 5 days ago
    now = datetime.now(timezone.utc)
    due_date = now - timedelta(days=5)
    issue_date = now - timedelta(days=19)
    
    with db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO issues (book_id, user_id, status, issue_date, due_date) VALUES (%s, %s, 'issued', %s, %s) RETURNING sl_no",
                (book_id, 'test_user_1', issue_date, due_date)
            )
            issue_id = cur.fetchone()[0]
            conn.commit()

    # Verify current fine (should be 5)
    with db_connection() as conn:
        res = conn.execute("SELECT fine_amount FROM issues_with_fines WHERE sl_no = %s", (issue_id,)).fetchone()
        print(f"Current Fine (5 days late): ₹{res['fine_amount']}")

    # 2. Student requests return TODAY
    Request.create_request(book_id, 'test_user_1', 'return')
    Issue.mark_return_requested(issue_id, now)
    
    # 3. Verify fine STOPS at 5 even if we "wait"
    with db_connection() as conn:
        res = conn.execute("SELECT fine_amount FROM issues_with_fines WHERE sl_no = %s", (issue_id,)).fetchone()
        print(f"Fine after return request: ₹{res['fine_amount']} (Expected: 5)")

def test_scenario_2_3(book_id):
    print("\n--- Scenario 2 & 3: Renewal Window & Fine payment ---")
    now = datetime.now(timezone.utc)
    
    # User 1: 3 days late (Window: 7 days, so should succeed)
    due_date_ok = now - timedelta(days=3)
    # User 2: 8 days late (Window: 7 days, so should fail)
    due_date_fail = now - timedelta(days=8)
    
    with db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO issues (book_id, user_id, status, due_date) VALUES (%s, %s, 'issued', %s) RETURNING sl_no", (book_id, 'test_user_1', due_date_ok))
            cur.execute("INSERT INTO issues (book_id, user_id, status, due_date) VALUES (%s, %s, 'issued', %s) RETURNING sl_no", (book_id, 'test_user_2', due_date_fail))
            conn.commit()

    # Try renewal for user 1 (3 days late)
    # This simulation doesn't use the flask route but the logic inside it
    with db_connection() as conn:
        issue = conn.execute("SELECT * FROM issues WHERE user_id = 'test_user_1' AND status = 'issued'").fetchone()
        if now <= (issue['due_date'] + timedelta(days=7)):
            print("User 1 (3 days late): Within renewal window. OK.")
        else:
            print("User 1: FAILED window check unexpectedly.")

    # Try renewal for user 2 (8 days late)
    with db_connection() as conn:
        issue = conn.execute("SELECT * FROM issues WHERE user_id = 'test_user_2' AND status = 'issued'").fetchone()
        if now <= (issue['due_date'] + timedelta(days=7)):
            print("User 2 (8 days late): FAILED - window check erroneously passed.")
        else:
            print("User 2 (8 days late): Outside renewal window. CORRECTLY BLOCKED.")

def test_scenario_4(book_id):
    print("\n--- Scenario 4: Second Renewal Restriction ---")
    now = datetime.now(timezone.utc)
    
    # User 1 has already renewed once (renewal_count = 1)
    with db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO issues (book_id, user_id, status, renewal_count, due_date) VALUES (%s, %s, 'issued', 1, %s) RETURNING sl_no", (book_id, 'test_user_1', now + timedelta(days=5)))
            conn.commit()
    
    # User 2 makes a pending request for the same book
    Request.create_request(book_id, 'test_user_2', 'reserve')
    
    # Check if User 1 can renew again
    with db_connection() as conn:
        issue = conn.execute("SELECT renewal_count FROM issues WHERE user_id = 'test_user_1' AND status = 'issued'").fetchone()
        competing = conn.execute("SELECT sl_no FROM requests WHERE book_id = %s AND status = 'pending' AND requested_by != 'test_user_1'", (book_id,)).fetchone()
        
        if issue['renewal_count'] == 1 and competing:
            print("User 1 (2nd renewal): Competing request found. RENEWAL BLOCKED as per rule.")
        else:
            print("User 1 (2nd renewal): FAILED to detect competing request.")

if __name__ == "__main__":
    b_id = setup_test_data()
    test_scenario_1(b_id)
    test_scenario_2_3(b_id)
    test_scenario_4(b_id)
