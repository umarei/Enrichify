# Company Data Enrichment

This project extracts company data from an SQLite database, enriches it using the LinkedIn Bulk Data Scraper API, and stores the enriched data in a new table.

## Files

- `setup_db.py`: Script to set up the database and insert initial data.
- `main.py`: Script to retrieve and enrich company data using LinkedIn Bulk Data Scraper API.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)
- SQLite

## Usage

1. Run `setup_db.py` to set up the database and insert initial data:
   ```bash
   python setup_db.py




### Additional Tips

- **.gitignore**: Consider adding a `.gitignore` file to exclude files that should not be included in the repository (e.g., virtual environment files, database files). For example:

  ```bash
  __pycache__/
  *.pyc
  *.pyo
  *.db
