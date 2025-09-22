import pandas as pd
from datetime import datetime

class DataCleaner:
    def __init__(self):
        pass

    def clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        # حذف ردیف‌های کاملا خالی
        df.dropna(how='all', inplace=True)

        # حذف ردیف‌های تکراری
        df.drop_duplicates(inplace=True)

        # استاندارد کردن نام ستون‌ها
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # تمیز کردن فضای خالی در داده‌های متنی
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.strip()

        # اصلاح تاریخ‌ها (در صورت وجود ستون date یا مشابه)
        for col in df.columns:
            if "date" in col:
                try:
                    df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
                except Exception:
                    pass

 
        # جایگزینی Null بر اساس نوع ستون
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(0)
            else:
                df[col] = df[col].fillna("")


        return df

if __name__ == "__main__":
    cleaner = DataCleaner()
    sample_data = pd.DataFrame({
        " Name ": [" Ali ", "Sara", None, "Ali "],
        "Age": [30, 25, None, 30],
        "City": ["Tehran", " Shiraz ", "Tabriz", "Tehran"],
        "Ingest Date": ["2025-09-22", "22-09-2025", None, "2025/09/22"]
    })
    print("📌 Before Cleaning:")
    print(sample_data)

    cleaned = cleaner.clean_dataframe(sample_data)
    print("\n✅ After Cleaning:")
    print(cleaned)
