import psycopg2
import pandas as pd
from config import DB_CONFIG

def save_to_db(df: pd.DataFrame, table_name: str):
    """
    Save a pandas DataFrame into a PostgreSQL database.
    If the table exists, it will be replaced.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # پاک کردن جدول قبلی (اگر وجود داشته باشد)
    cur.execute(f"DROP TABLE IF EXISTS {table_name};")
    conn.commit()

    # ایجاد جدول جدید بر اساس ستون‌های DataFrame
    columns = ", ".join([f"{col} TEXT" for col in df.columns])
    cur.execute(f"CREATE TABLE {table_name} ({columns});")
    conn.commit()

    # ذخیره داده‌ها ردیف به ردیف
    for _, row in df.iterrows():
        values = [str(v) for v in row.tolist()]
        placeholders = ", ".join(["%s"] * len(values))
        cur.execute(
            f"INSERT INTO {table_name} VALUES ({placeholders});",
            values
        )

    conn.commit()
    cur.close()
    conn.close()

