import sqlite3
import pandas as pd

def save_to_db(df: pd.DataFrame, db_name: str, table_name: str):
"""
Save a pandas DataFrame into an SQLite database.
If the table exists, it will be replaced.
"""
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists="replace", index=False)
conn.close()
