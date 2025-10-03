import json
import re
from pathlib import Path
import argparse

profiles_path = Path(__file__).parent / "profiles.json"
with open(profiles_path, "r", encoding="utf-8") as f:
    FILTER_PROFILES = json.load(f)

TEST_DATA = [
    {"lang": "en", "category": "news", "title": "Breaking News 1"},
    {"lang": "en", "category": "news", "title": "Breaking News 2"},

    {"lang": "fa", "category": "technology", "title": "فناوری روز ایران"},
    {"lang": "fa", "category": "technology", "title": "نوآوری\u200cهای هوش مصنوعی"},
    {"lang": "fa", "category": "technology", "title": "پیشرفت\u200cهای رباتیک"},

    {"lang": "de", "category": "news", "title": "Nachrichten aus Berlin"},
    {"lang": "de", "category": "news", "title": "Technologie Nachrichten"},

    {"lang": "fa", "category": "general", "title": "اخبار عمومی"},
    {"lang": "en", "category": "general", "title": "General News"},
    {"lang": "de", "category": "general", "title": "Allgemeine Nachrichten"}
]

def normalize_val(val):
    s = str(val).strip().lower()
    s = re.sub(r'[\u200c\u200b]', '', s)
    return s

def process_query(filters):
    results = []
    for record in TEST_DATA:
        match = True
        for key, val in filters.items():
            rec_val_raw = record.get(key)

            # اگر رکورد این فیلد رو نداره، فیلتر رو نادیده بگیر
            if rec_val_raw is None:
                continue

            rec_val = normalize_val(rec_val_raw)
            val_norm = normalize_val(val)

            # اگر فیلتر مقدار لیستی داره
            if isinstance(val_norm, list):
                if rec_val not in val_norm:
                    match = False
                    break
            # اگر فقط یک مقدار ساده است
            else:
                if rec_val != val_norm:
                    match = False
                    break

        if match:
            results.append(record)
    return results


def run_query(profile_name, output_json):
    if profile_name not in FILTER_PROFILES:
        print(f"Profile '{profile_name}' not found.")
        return

    filters = FILTER_PROFILES[profile_name]
    results = process_query(filters)

    if output_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            print(f"{r['lang']} | {r['category']} | {r['title']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query Engine")
    parser.add_argument("profile", help="Profile name from profiles.json")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    run_query(args.profile, args.json)
