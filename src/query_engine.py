import argparse
import pandas as pd
from .db_connector import connect_db

def build_conditions(args):
    conditions = []

    if args.cities:
        cities_list = "', '".join([c.lower() for c in args.cities])
        conditions.append(f"LOWER(city) IN ('{cities_list}')")

    if args.min_age is not None:
        conditions.append(f"age >= {args.min_age}")

    if args.max_age is not None:
        conditions.append(f"age <= {args.max_age}")

    if args.names:
        names_list = "', '".join([n.lower() for n in args.names])
        conditions.append(f"LOWER(name) IN ('{names_list}')")

    if args.start_date:
        conditions.append(f"record_date >= '{args.start_date}'")

    if args.end_date:
        conditions.append(f"record_date <= '{args.end_date}'")

    return " AND ".join(conditions) if conditions else "1=1"


def interactive_input():
    cities = input("Enter cities (comma-separated) or leave blank: ").strip()
    cities = cities.split(",") if cities else None

    min_age = input("Enter minimum age or leave blank: ").strip()
    min_age = int(min_age) if min_age else None

    max_age = input("Enter maximum age or leave blank: ").strip()
    max_age = int(max_age) if max_age else None

    names = input("Enter names (comma-separated) or leave blank: ").strip()
    names = names.split(",") if names else None

    start_date = input("Enter start date (YYYY-MM-DD) or leave blank: ").strip() or None
    end_date = input("Enter end date (YYYY-MM-DD) or leave blank: ").strip() or None

    return argparse.Namespace(
        cities=[c.strip() for c in cities] if cities else None,
        min_age=min_age,
        max_age=max_age,
        names=[n.strip() for n in names] if names else None,
        start_date=start_date,
        end_date=end_date
    )

def filter_and_export(args):
    engine = connect_db()
    where_clause = build_conditions(args)
    query = f"SELECT * FROM data_records WHERE {where_clause};"

    df = pd.read_sql(query, engine)
    
    if df.empty:
        print("⚠️ No matching records found.")
        return

    print(df.head())  # نمایش خلاصه‌ای از داده‌ها
    df.to_csv("data/filtered_data.csv", index=False)
    df.to_excel("data/filtered_data.xlsx", index=False)
    print(f"✅ Exported {len(df)} records to data/filtered_data.csv and data/filtered_data.xlsx.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter PostgreSQL data with CLI or interactive mode")
    parser.add_argument("--cities", nargs="+", help="Cities to filter")
    parser.add_argument("--min_age", type=int, help="Minimum age")
    parser.add_argument("--max_age", type=int, help="Maximum age")
    parser.add_argument("--names", nargs="+", help="Names to filter")
    parser.add_argument("--start_date", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end_date", help="End date (YYYY-MM-DD)")
    
    args = parser.parse_args()

    # اگر هیچ آرگومان داده نشد، حالت تعاملی اجرا می‌شود
    if not any(vars(args).values()):
        args = interactive_input()

    filter_and_export(args)
