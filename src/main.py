from cleaner import clean_data
from database import save_to_db
from exporter import export_data

def main():
    input_file = "../data/sample.csv" # مسیر فایل نمونه
    db_file = "../data/data_bot.db" # مسیر دیتابیس
    table_name = "dataset"
    output_file = "../data/cleaned.csv" # مسیر فایل خروجی

# 1️⃣ پاک‌سازی داده
    df = clean_data(input_file)
    print("✅ Data cleaned.")

# 2️⃣ ذخیره در دیتابیس
    save_to_db(df, table_name)
    print(f"✅ Data saved to database: {db_file}")

# 3️⃣ خروجی گرفتن
    export_data(df, output_file, format="csv")
    print(f"✅ Data exported to {output_file}")

if __name__ == "__main__":
    main()
