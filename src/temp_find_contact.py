import os
import sys
# Add src to path to handle relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.clients import notion as nc
from src import config

def find_contact_number(name):
    """Finds a contact's phone number by name."""
    notion_client = nc.get_notion_client()
    db_id = os.getenv('WHATSAPP_CONTACTS_DB_ID')
    if not db_id:
        print("WHATSAPP_CONTACTS_DB_ID not found in .env")
        return

    results = notion_client.databases.query(
        database_id=db_id,
        filter={'property': 'Name', 'title': {'equals': name}}
    ).get('results', [])

    if results:
        number = results[0].get('properties', {}).get('Number', {}).get('phone_number')
        print(number)
    else:
        print("Not Found")

if __name__ == "__main__":
    find_contact_number("אמא") 