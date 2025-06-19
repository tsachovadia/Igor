import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Application Configuration
APP_NAME = os.getenv("APP_NAME", "Igor")

# API Keys
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GREEN_API_ID_INSTANCE = os.getenv("GREEN_API_ID_INSTANCE")
GREEN_API_API_TOKEN_INSTANCE = os.getenv("GREEN_API_API_TOKEN_INSTANCE")

# Notion Database IDs
IGOR_LOG_DB_ID = os.getenv("IGOR_LOG_DB_ID")
GMAIL_DB_ID = os.getenv("GMAIL_DB_ID")
UB_PROJECTS_DB_ID = os.getenv("UB_PROJECTS_DB_ID")
WHATSAPP_CONTACTS_DB_ID = os.getenv("WHATSAPP_CONTACTS_DB_ID")

# Example environment variable
# We will add real ones like NOTION_API_KEY here later 