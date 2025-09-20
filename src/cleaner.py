import pandas as pd

def clean_data(file_path: str) -> pd.DataFrame:
"""
Read CSV, drop missing values and duplicates,
then return the cleaned dataframe.
"""
df = pd.read_csv(file_path)
df = df.dropna() # حذف ردیف‌های ناقص
df = df.drop_duplicates() # حذف داده‌های تکراری
return df
