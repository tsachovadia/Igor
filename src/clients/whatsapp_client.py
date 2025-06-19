# This file will contain the client and functions for interacting with the Green-API for WhatsApp.

# We will add functions here to:
# - Initialize the API client
# - Send messages
# - Receive and process incoming webhooks 

from whatsapp_api_client_python import API
import config

def get_whatsapp_client():
    """Initializes and returns the Green-API client."""
    if not config.GREEN_API_ID_INSTANCE or not config.GREEN_API_API_TOKEN_INSTANCE:
        raise ValueError("Green-API credentials are not set in your .env file.")
    
    return API.GreenApi(config.GREEN_API_ID_INSTANCE, config.GREEN_API_API_TOKEN_INSTANCE)

def get_instance_state(client: API.GreenApi):
    """Gets the state of the connected WhatsApp instance."""
    return client.account.getStateInstance()

def get_contacts(client: API.GreenApi):
    """Gets the list of all contacts from WhatsApp."""
    return client.serviceMethods.getContacts()

def update_instance_settings(client: API.GreenApi, settings: dict):
    """Updates the instance settings with the provided dictionary."""
    return client.account.setSettings(settings)

def send_whatsapp_message(client: API.GreenApi, to_number: str, message: str):
    """
    Sends a text message to a specified WhatsApp number.
    The number should be in the format '79991234567'.
    """
    # Green-API requires the chat ID to be the number followed by @c.us
    chat_id = f"{to_number}@c.us"
    return client.sending.sendMessage(chat_id, message) 