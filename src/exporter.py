import psycopg2
import pandas as pd
from psycopg2 import OperationalError

DB_CONFIG = {
    "host": "localhost",
    "user": "shahpari2kht",
    "password": "1017190N@nook",
    "database": "data_bot"
}

def create_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except OperationalError as e:
        print(f"❌ Connection error: {e}")
        return None

def export_to_csv(query, file_path):
    conn = create_connection()
    if conn:
        df = pd.read_sql_query(query, conn)
        df.to_csv(file_path, index=False)
        print(f"✅ Data exported to {file_path}")
        conn.close()

def export_to_excel(query, file_path):
    conn = create_connection()
    if conn:
        df = pd.read_sql_query(query, conn)
        df.to_excel(file_path, index=False)
        print(f"✅ Data exported to {file_path}")
        conn.close()

if __name__ == "__main__":
    sql_query = "SELECT * FROM data_records ORDER BY id DESC"
    export_to_csv(sql_query, "data/exported_data.csv")
    export_to_excel(sql_query, "data/exported_data.xlsx")
