import os
import sys
import json

# Add the 'src' directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from clients import whatsapp_client as wc
from src import config

def discover_history(chat_id):
    """
    Attempts to fetch chat history with more detailed logging.
    """
    print(f"Attempting to fetch history for chat: {chat_id}")
    
    try:
        client = wc.get_whatsapp_client()
        
        # Try to get the last 100 messages to be more thorough
        response = client.journals.getChatHistory(chat_id, 100)
        
        print(f"API Response Code: {response.code}")
        print("--- RAW RESPONSE DATA ---")
        print(response.data)
        print("--- END RAW RESPONSE ---")

        if response.code == 200 and response.data:
             print("\n[SUCCESS] Successfully fetched chat history.")
        else:
            print(f"\n[FAILURE] Failed to fetch chat history. Error: {response.error}")

    except Exception as e:
        print(f"\n[ERROR] An unexpected script error occurred: {e}")

if __name__ == "__main__":
    target_number = "972546781344"
    target_chat_id = f"{target_number}@c.us"
    discover_history(target_chat_id) 