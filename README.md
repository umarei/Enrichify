# Enrichify

Enrichify is a Python project that extracts company data from an SQL database, enriches it using the LinkedIn Bulk Data Scraper API, and stores the enriched data in a new database table.

## Features

- Extracts company information from a SQLite database.
- Uses the LinkedIn Bulk Data Scraper API to enrich company data.
- Stores enriched data in a new database table.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/enrichify.git
    cd enrichify
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set up the database:
    ```bash
    python setup_db.py
    ```

2. Run the main script to fetch and enrich data:
    ```bash
    python main.py
    ```
