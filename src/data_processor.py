import pandas as pd
import psycopg2
from psycopg2.extras import Json
from .db_connector import connect_db

def process_and_ingest(file_path):
    df = pd.read_csv(file_path)

    # پاکسازی داده
    df.dropna(subset=['name', 'city', 'age', 'record_date'], inplace=True)
    df['age'] = df['age'].astype(int)
    df['record_date'] = pd.to_datetime(df['record_date']).dt.date

    conn = connect_db()
    cur = conn.cursor()

    for _, row in df.iterrows():
        # تبدیل ردیف به دیکشنری و رشته کردن تاریخ‌ها برای JSON
        record_dict = row.to_dict()
        for key, value in record_dict.items():
            if hasattr(value, 'isoformat'):
                record_dict[key] = value.isoformat()

        cur.execute("""
            INSERT INTO data_records (name, city, age, record_date, source, raw_content)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row['name'],
            row['city'],
            row['age'],
            row['record_date'],
            file_path,
            Json(record_dict)
        ))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ {len(df)} records inserted from {file_path}.")

if __name__ == "__main__":
    process_and_ingest("data/sample.csv")
