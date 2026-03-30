import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname='csconnect', user='postgres', password='@mugdham', host='127.0.0.1')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Check all tables and their columns
cur.execute("""
    SELECT table_name, string_agg(column_name, ', ' ORDER BY ordinal_position) as cols
    FROM information_schema.columns
    WHERE table_schema = 'public'
    GROUP BY table_name
    ORDER BY table_name
""")
rows = cur.fetchall()
for r in rows:
    print(f"{r['table_name']}: {r['cols']}")

conn.close()
