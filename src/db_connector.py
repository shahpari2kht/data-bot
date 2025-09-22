import psycopg2
from psycopg2 import sql

def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="data_bot",
        user="shahpari2kht",
        password="1017190N@nook"
    )
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()

    create_query = """
    CREATE TABLE IF NOT EXISTS data_records (
        id SERIAL PRIMARY KEY,
        name TEXT,
        city TEXT,
        age INTEGER,
        record_date DATE,
        source TEXT,
        ingest_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        raw_content JSONB,
        processed_flag BOOLEAN DEFAULT FALSE,
        notes TEXT
    );
    """
    cur.execute(create_query)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Table 'data_records' ready.")

if __name__ == "__main__":
    create_table()
