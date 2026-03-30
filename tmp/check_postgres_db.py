import psycopg2
conn = psycopg2.connect(dbname='postgres', user='postgres', password='@mugdham', host='127.0.0.1')
cur = conn.cursor()
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
rows = cur.fetchall()
print('Tables in postgres db:', [r[0] for r in rows])
conn.close()
