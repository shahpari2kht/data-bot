# 🚀 Data Bot | ربات داده

**Data Bot** is a lightweight Python query engine designed to filter and process structured profiles based on configurable filters.  
It supports multiple languages and provides a simple command-line interface for testing and development.

**دیتابوت** یک موتور جستجوی سبک و سریع نوشته شده با پایتون است که برای فیلتر و پردازش پروفایل‌های ساختاریافته بر اساس فیلترهای قابل تنظیم طراحی شده است.  
این ابزار چندزبانه است و رابط خط فرمان ساده برای توسعه و تست دارد.

---

## ✨ Features | ویژگی‌ها

- 🌐 **Multi language support:** Persian, German, English  
  پشتیبانی چند زبانه: فارسی، آلمانی، انگلیسی
- ⚡ **Robust filter logic** that gracefully ignores missing fields  
  منطق فیلترینگ قوی که فیلدهای ناقص را نادیده می‌گیرد
- 🧪 **Mock `TEST_DATA`** included for development & testing  
  داده‌های نمونه `TEST_DATA` برای توسعه و تست
- 📂 **Profiles stored in `profiles.json`** and executed via command line  
  پروفایل‌ها در `profiles.json` ذخیره شده و از طریق خط فرمان اجرا می‌شوند
- 🛠️ **Modular architecture** for easy extension  
  معماری ماژولار برای افزودن قابلیت‌های جدید

---

## 🗂 Project Structure | ساختار پروژه

data-bot/
├── src/
│ ├── init.py
│ ├── cleaner.py
│ ├── config.py
│ ├── data_cleaner.py
│ ├── data_cleaning.py
│ ├── data_processor.py
│ ├── database.py
│ ├── db_connector.py
│ ├── exporter.py
│ ├── file_intake.py
│ ├── main.py
│ └── query_engine.py
├── tests/
│ └── test_imports.py
├── .github/
│ ├── workflows/ci.yaml
│ ├── ISSUE_TEMPLATE/bug_report.md
│ └── PULL_REQUEST_TEMPLATE.md
├── profiles.json
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
└── requirements.txt


> ⚠️ **Note | نکته:** Remove `query_engine.py.save` and any `.zip` files to keep the repository clean.  
> فایل‌های بکاپ مانند `query_engine.py.save` و فایل‌های `.zip` باید حذف شوند تا مخزن مرتب بماند.

---

## 🏃 How to Run | نحوه اجرا

1. **Activate the virtual environment | فعال‌سازی محیط مجازی:**

```bash
source venv/bin/activate


Run a specific profile | اجرای یک پروفایل خاص:

python src/query_engine.py profile_tech_fa --json

💡 Example Output | مثال خروجی
[
  {"id": 1, "category": "Tech", "lang": "fa", "date": "2025-09-21"},
  {"id": 2, "category": "Tech", "lang": "fa", "date": "2025-09-25"}
]

🖼 Screenshot | تصویر خروجی


تصویر بالا نمونه خروجی نهایی دیتابوت را نشان می‌دهد.

🚀 Future Improvements | توسعه‌های آتی

📊 Integrate real-world datasets
افزودن داده‌های واقعی و بزرگ

🗓 Add date filtering logic for date_range
اضافه کردن فیلتر تاریخ برای محدوده‌های زمانی

🐳 Deploy as an API or Docker container
انتشار به‌صورت API یا کانتینر داکر

✅ Add comprehensive unit tests for all modules
اضافه کردن تست‌های واحد کامل برای تمامی ماژول‌ها

✍️ Author | نویسنده

Parisa Mohammadzadeh | پریسا محمدزاده
