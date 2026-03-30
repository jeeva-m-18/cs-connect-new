import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def get_schema(url):
    print(f"Fetching schema for {url.split('@')[-1] if '@' in url else 'configured_url'}")
    try:
        conn = psycopg2.connect(url)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            query = """
            SELECT 
                table_name, 
                column_name, 
                data_type 
            FROM 
                information_schema.columns 
            WHERE 
                table_schema = 'public' 
            ORDER BY 
                table_name, ordinal_position;
            """
            cur.execute(query)
            rows = cur.fetchall()
            schema = {}
            for row in rows:
                table = row['table_name']
                if table not in schema:
                    schema[table] = []
                schema[table].append((row['column_name'], row['data_type']))
            return schema
    except Exception as e:
        print(f"Error: {e}")
        return None

local_url = os.environ.get("LOCAL_DATABASE_URL")
neon_url = os.environ.get("NEON_DATABASE_URL")

local_schema = get_schema(local_url)
neon_schema = get_schema(neon_url)

if local_schema and neon_schema:
    print("\n--- Comparison Table List ---")
    local_tables = set(local_schema.keys())
    neon_tables = set(neon_schema.keys())

    only_local = sorted(list(local_tables - neon_tables))
    only_neon = sorted(list(neon_tables - local_tables))
    common_tables = sorted(list(local_tables & neon_tables))

    print(f"Count: Local ({len(local_tables)}), Neon ({len(neon_tables)})")
    
    if only_local:
        print(f"Tables ONLY in LOCAL ({len(only_local)}): {only_local}")
    else:
        print("No tables only in LOCAL.")
        
    if only_neon:
        print(f"Tables ONLY in NEON ({len(only_neon)}): {only_neon}")
    else:
        print("No tables only in NEON.")

    print("\n--- Schema Mismatches in Common Tables ---")
    mismatch_count = 0
    for table in common_tables:
        local_cols = local_schema[table]
        neon_cols = neon_schema[table]
        if local_cols != neon_cols:
            mismatch_count += 1
            print(f"\nTable '{table}':")
            # print(f"  LOCAL: {local_cols}")
            # print(f"  NEON : {neon_cols}")
            
            # Find specific differences
            local_col_dict = dict(local_cols)
            neon_col_dict = dict(neon_cols)
            
            only_in_local_cols = set(local_col_dict.keys()) - set(neon_col_dict.keys())
            only_in_neon_cols = set(neon_col_dict.keys()) - set(local_col_dict.keys())
            
            if only_in_local_cols:
                print(f"  Columns only in LOCAL: {only_in_local_cols}")
            if only_in_neon_cols:
                print(f"  Columns only in NEON : {only_in_neon_cols}")
            
            for col in set(local_col_dict.keys()) & set(neon_col_dict.keys()):
                if local_col_dict[col] != neon_col_dict[col]:
                    print(f"  Type mismatch for '{col}': LOCAL={local_col_dict[col]}, NEON={neon_col_dict[col]}")

    if mismatch_count == 0:
        print("No schema mismatches found in common tables.")
    else:
        print(f"\nFound {mismatch_count} tables with schema mismatches.")
else:
    print("Failed to fetch one or both schemas.")
