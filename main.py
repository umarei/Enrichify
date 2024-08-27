import sqlite3
import requests

# Connect to SQLite database
conn = sqlite3.connect('company_data.db')
c = conn.cursor()

# Fetch company data
c.execute("SELECT * FROM companies")
companies = c.fetchall()

# Check if companies are retrieved
if companies:
    urls = [company[2] for company in companies]  # Extract LinkedIn URLs

    # Set up the LinkedIn Bulk Data Scraper API request
    url = 'https://linkedin-bulk-data-scraper.p.rapidapi.com/companies'

    headers = {
        "x-rapidapi-host": "linkedin-bulk-data-scraper.p.rapidapi.com",
        "x-rapidapi-key": "5025f4d7fcmsh24ce687f705dc49p19579fjsn3e2ff2e34f26",
        "Content-Type": "application/json"
    }
    body = {
        "links": urls  # Updated parameter name
    }

    try:
        # Make the API request
        response = requests.post(url, headers=headers, json=body)

        # Check the response status
        if response.status_code == 200:
            enriched_data = response.json()
            print("Enriched data:", enriched_data)

            # Creating a new table for enriched data if it doesn't exist
            c.execute('''CREATE TABLE IF NOT EXISTS enriched_companies
                         (company_id INTEGER PRIMARY KEY,
                          company_name TEXT,
                          enriched_info TEXT)''')

            # Insert enriched data into the new table
            for company in companies:
                company_id, company_name, company_linkedin_url = company
                # Assume enriched_data is a dictionary with company URLs as keys
                enriched_info = enriched_data.get(company_linkedin_url, "No data found")
                c.execute("INSERT OR REPLACE INTO enriched_companies (company_id, company_name, enriched_info) VALUES (?, ?, ?)",
                          (company_id, company_name, str(enriched_info)))

            conn.commit()
            print("Enriched data has been inserted into the database.")
        else:
            print("Failed to retrieve enriched data. HTTP Status Code:", response.status_code)
            print("Response Content:", response.content)

    except requests.exceptions.RequestException as e:
        print("Error during API request:", e)

else:
    print("No company data found in the database.")

# Close the database connection
conn.close()
