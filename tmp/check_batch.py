import psycopg2
conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/cs_connect_v2")
cur = conn.cursor()
try:
    cur.execute("SELECT user_id, name, role, batch FROM users WHERE role='student' LIMIT 5;")
    for row in cur.fetchall(): print(row)
except Exception as e:
    print(e)
