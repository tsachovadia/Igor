import os
import sys
import json

# Add the 'src' directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from clients.notion import get_notion_client

DATABASE_ID = "2168615a-8537-8146-8a6e-cc5cf9c3453d"
OUTPUT_FILE = "notion_contacts.json"

def fetch_all_contacts():
    """
    Fetches all contacts from the Notion database and saves them to a JSON file.
    """
    notion = get_notion_client()
    all_results = []
    has_more = True
    start_cursor = None
    total_contacts = 0

    print("Starting to fetch contacts from Notion...")

    while has_more:
        try:
            if start_cursor:
                response = notion.databases.query(
                    database_id=DATABASE_ID,
                    start_cursor=start_cursor
                )
            else:
                response = notion.databases.query(database_id=DATABASE_ID)

            results = response.get("results", [])
            all_results.extend(results)
            total_contacts += len(results)
            
            print(f"Fetched {len(results)} contacts. Total so far: {total_contacts}")

            has_more = response.get("has_more")
            start_cursor = response.get("next_cursor")

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    print(f"\nFinished fetching. Total contacts found: {total_contacts}")

    # Save to JSON file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=4)

    print(f"All contacts have been saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_all_contacts() 