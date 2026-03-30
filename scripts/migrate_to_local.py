"""
Migrates all data from Neon Cloud PostgreSQL to Local PostgreSQL.
Run once: python scripts/migrate_to_local.py
"""
import psycopg2
import psycopg2.extras
import json
import sys

NEON_URL = "postgresql://neondb_owner:npg_zsf9Rtkm6YBT@ep-long-water-a1yyxfck-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"
LOCAL = dict(dbname="postgres", user="postgres", password="@mugdham", host="127.0.0.1")
LOCAL_DB = "csconnect"

def run(msg):
    print(msg, end="... ", flush=True)

# ---------- 1. Create the local DB ----------
run("Creating local database 'csconnect'")
admin = psycopg2.connect(**LOCAL)
admin.autocommit = True
cur = admin.cursor()
cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{LOCAL_DB}'")
if not cur.fetchone():
    cur.execute(f"CREATE DATABASE {LOCAL_DB}")
cur.close()
admin.close()
print("OK")

# ---------- 2. Connect to both ----------
run("Connecting to Neon")
src = psycopg2.connect(NEON_URL)
src.autocommit = False
print("OK")

run("Connecting to local DB")
dst = psycopg2.connect(dbname=LOCAL_DB, user="postgres", password="@mugdham", host="127.0.0.1")
dst.autocommit = False
print("OK")

src_cur = src.cursor(cursor_factory=psycopg2.extras.DictCursor)
dst_cur = dst.cursor()

# ---------- 3. Get ordered table list from Neon ----------
run("Fetching table list")
src_cur.execute("""
    SELECT table_name FROM information_schema.tables
    WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
    ORDER BY table_name
""")
tables = [r[0] for r in src_cur.fetchall()]
print(f"Found {len(tables)} tables: {tables}")

# ---------- 4. Get CREATE statements from Neon via pg_dump logic ----------
run("Fetching schema DDL")
src_cur.execute("""
    SELECT table_name,
           string_agg(
               column_name || ' ' || 
               CASE 
                   WHEN data_type = 'integer' AND column_default LIKE 'nextval%' THEN 'SERIAL'
                   WHEN data_type IN ('character varying') THEN 'TEXT'
                   WHEN data_type IN ('character') THEN 'TEXT'
                   ELSE data_type
               END ||
               CASE WHEN is_nullable = 'NO' AND column_default IS NULL THEN ' NOT NULL' ELSE '' END ||
               CASE WHEN column_default IS NOT NULL AND column_default NOT LIKE 'nextval%' 
                    THEN ' DEFAULT ' || column_default ELSE '' END,
               ', ' ORDER BY ordinal_position
           ) AS cols
    FROM information_schema.columns
    WHERE table_schema = 'public'
    GROUP BY table_name
""")
schema_rows = {r[0]: r[1] for r in src_cur.fetchall()}
print("OK")

# ---------- 5. Replicate schema on local ----------
run("Creating tables on local DB")
for tbl in tables:
    cols = schema_rows.get(tbl, "")
    dst_cur.execute(f"DROP TABLE IF EXISTS {tbl} CASCADE")
    dst_cur.execute(f"CREATE TABLE IF NOT EXISTS {tbl} ({cols})")
dst.commit()
print("OK")

# ---------- 6. Copy data row by row ----------
total_rows = 0
for tbl in tables:
    src_cur.execute(f"SELECT * FROM {tbl}")
    rows = src_cur.fetchall()
    if not rows:
        print(f"  {tbl}: empty, skipped")
        continue

    cols = [d[0] for d in src_cur.description]
    col_str = ", ".join(cols)
    placeholders = ", ".join(["%s"] * len(cols))

    inserted = 0
    for row in rows:
        values = []
        for v in row:
            if isinstance(v, (dict, list)):
                values.append(json.dumps(v))
            else:
                values.append(v)
        try:
            dst_cur.execute(f"INSERT INTO {tbl} ({col_str}) VALUES ({placeholders})", values)
            inserted += 1
        except Exception as e:
            dst.rollback()
            print(f"  WARNING: skipped row in {tbl}: {e}")

    dst.commit()
    total_rows += inserted
    print(f"  {tbl}: {inserted}/{len(rows)} rows copied")

# ---------- 7. Reset sequences ----------
run("Resetting sequences")
src_cur.execute("""
    SELECT sequence_name FROM information_schema.sequences
    WHERE sequence_schema = 'public'
""")
seqs = [r[0] for r in src_cur.fetchall()]
for seq in seqs:
    try:
        src_cur.execute(f"SELECT last_value FROM {seq}")
        lv = src_cur.fetchone()[0]
        dst_cur.execute(f"SELECT setval('{seq}', {lv})")
    except Exception:
        pass
dst.commit()
print("OK")

src.close()
dst.close()

print(f"\n✅ Migration complete! {total_rows} total rows copied across {len(tables)} tables.")
print("Now update your .env file: LOCAL_DATABASE_URL=postgresql://postgres:@mugdham@127.0.0.1:5432/csconnect")
