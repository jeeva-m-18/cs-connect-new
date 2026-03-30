import os
from dotenv import load_dotenv
load_dotenv()

url = os.environ.get("LOCAL_DATABASE_URL")
print("LOCAL_DATABASE_URL:", url)

from database import db_connection
with db_connection() as conn:
    row = conn.execute("SELECT current_database()").fetchone()
    print("Connected to:", row[0])
