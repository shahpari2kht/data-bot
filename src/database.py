import pandas as pd
import psycopg2

DB_CONFIG = {
    "dbname": "data_bot_db",
    "user": "shahpari2kht",
    "password": "1017190N@nook",
    "host": "localhost",
    "port": 5432
}

def save_to_db(df: pd.DataFrame, table_name: str):
    """
    Save a pandas DataFrame into a PostgreSQL table.
    If the table exists, it will be replaced.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    conn.commit()

    # ساخت جدول با تمام ستون‌ها به‌صورت TEXT
    columns = ", ".join([f"{col} TEXT" for col in df.columns])
    cursor.execute(f"CREATE TABLE {table_name} ({columns});")
    conn.commit()

    # درج داده‌ها
    for _, row in df.iterrows():
        values = "', '".join([str(val) for val in row])
        cursor.execute(f"INSERT INTO {table_name} VALUES ('{values}');")

    conn.commit()
    cursor.close()
    conn.close()

