import os
import sys
import json

# Add the 'src' directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from clients import whatsapp_client as wc
from src import config

def discover_chat_data(chat_id):
    """
    Runs a series of Green-API functions for a specific chat ID and saves the raw output to a JSON file.
    """
    print(f"Starting data discovery for chat: {chat_id}")
    discovery_results = {}
    
    try:
        client = wc.get_whatsapp_client()
        
        # 1. Get Contact Info
        print("Fetching contact info...")
        contact_info = client.serviceMethods.getContactInfo(chat_id)
        discovery_results["getContactInfo"] = contact_info.data or contact_info.error
        
        # 2. Get Chat History (last 20 messages)
        print("Fetching chat history...")
        chat_history = client.journals.getChatHistory(chat_id, count=20)
        discovery_results["getChatHistory"] = chat_history.data or chat_history.error

        # Note: According to the docs, there isn't a simple "getChatInfo" method.
        # The most relevant data comes from the two calls above.

        # 3. Save to file
        file_path = "chat_discovery_results.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(discovery_results, f, ensure_ascii=False, indent=4)
            
        print(f"\n[SUCCESS] Data discovery complete. Results saved to '{file_path}'")

    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    target_number = "972546781344"
    target_chat_id = f"{target_number}@c.us"
    discover_chat_data(target_chat_id) 