import sqlite3

def setup_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('company_data.db')
    c = conn.cursor()

    # Create table for company data if it does not exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS companies (
            company_id INTEGER PRIMARY KEY, 
            company_name TEXT,
            company_linkedin_url TEXT
        )
    ''')

    # Insert Google data (if not already present)
    c.execute('''
        INSERT OR IGNORE INTO companies (company_id, company_name, company_linkedin_url)
        VALUES (?, ?, ?)
    ''', (1, 'Google', 'https://www.linkedin.com/company/google'))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
