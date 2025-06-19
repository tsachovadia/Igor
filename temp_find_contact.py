import os
import sys

# Add the 'src' directory to the path to allow for correct module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from clients import notion as nc
import config

def find_contact_number(name):
    """Finds a contact's phone number by name."""
    notion_client = nc.get_notion_client()
    db_id = os.getenv('WHATSAPP_CONTACTS_DB_ID')
    if not db_id:
        print("Error: WHATSAPP_CONTACTS_DB_ID not found in .env file.")
        return

    try:
        results = notion_client.databases.query(
            database_id=db_id,
            filter={'property': 'Name', 'title': {'equals': name}}
        ).get('results', [])

        if results:
            number = results[0].get('properties', {}).get('Number', {}).get('phone_number')
            print(number)
        else:
            print("Not Found")
    except Exception as e:
        print(f"An API error occurred: {e}")

if __name__ == "__main__":
    find_contact_number("אביב ניר צ4") 