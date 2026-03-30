import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def check_chatbot_db():
    url = os.environ.get("DATABASE_URL")
    if not url:
        print("DATABASE_URL not found in .env")
        return

    try:
        conn = psycopg2.connect(url)
        with conn.cursor() as cur:
            # 1. Check for pg_trgm extension
            cur.execute("SELECT extname FROM pg_extension WHERE extname = 'pg_trgm';")
            ext = cur.fetchone()
            if ext:
                print(f"Extension 'pg_trgm' is ENABLED.")
            else:
                print(f"Extension 'pg_trgm' is MISSING! Chatbot search will fail.")

            # 2. Check for faculty table
            cur.execute("SELECT count(*) FROM faculty;")
            count = cur.fetchone()[0]
            print(f"Faculty records: {count}")

            # 3. Check for 'HOD' in faculty table
            # Let's search for HOD specifically
            cur.execute("SELECT name, designation FROM faculty WHERE designation ILIKE '%HOD%' OR designation ILIKE '%Head%';")
            hods = cur.fetchall()
            if hods:
                print(f"HODs found: {hods}")
            else:
                print("No HODs found in faculty table.")

            # 4. Check website_content
            cur.execute("SELECT count(*) FROM website_content;")
            wc_count = cur.fetchone()[0]
            print(f"Website content records: {wc_count}")

            cur.execute("SELECT title FROM website_content WHERE title ILIKE '%HOD%' OR content ILIKE '%HOD%';")
            wc_hods = cur.fetchall()
            print(f"HODs in website_content: {wc_hods}")

        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_chatbot_db()
