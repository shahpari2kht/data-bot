# Data Bot

Data Bot is a lightweight query engine built in Python to filter and process structured profiles based on configurable filters.

## Features
- **Multi-language support** (Persian, German, English)
- Robust filter logic that ignores fields missing in data records
- Simple, mock `TEST_DATA` included for development & testing
- Profiles stored in `profiles.json` and executed via the command line

## Project Structure
src/
├── profiles.json        # Profile filter configurations
├── query_engine.py      # Query engine logic
└── query_engine.py.save # Backup

## How to Run
1. Activate the virtual environment:
   source venv/bin/activate

2. Run a specific profile:
   python src/query_engine.py profile_tech_fa --json

## Example Output
[
  {"id": 1, "category": "Tech", "lang": "fa", "date": "2025-09-21"},
  {"id": 2, "category": "Tech", "lang": "fa", "date": "2025-09-25"}
]

## Future Improvements
- Integrate real-world datasets
- Add date filtering logic for `date_range`
- Deploy as API and Docker container

## Author
**Parisa Mohammadzadeh**  
Languages: Persian (native), Kurdish, Arabic, German (B2), English (Intermediate)  
Location: Ilam, Iran → Planning migration to Germany.
