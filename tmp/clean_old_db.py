"""
Drops all stale app tables from the default 'postgres' database
so Flask never finds half-baked schema there by accident.
"""
import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password='@mugdham', host='127.0.0.1')
conn.autocommit = True
cur = conn.cursor()

cur.execute("""
    SELECT table_name FROM information_schema.tables
    WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
""")
tables = [r[0] for r in cur.fetchall()]
print(f"Dropping {len(tables)} stale tables from default 'postgres' db...")

for tbl in tables:
    try:
        cur.execute(f"DROP TABLE IF EXISTS {tbl} CASCADE")
        print(f"  Dropped: {tbl}")
    except Exception as e:
        print(f"  SKIP {tbl}: {e}")

conn.close()
print("Done. Default 'postgres' DB is now clean.")
