import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from rich.console import Console

console = Console()

# Define the scopes for all the services we want to access.
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/contacts.readonly",
]

def authenticate_google_account(account_email: str):
    """
    Handles the OAuth 2.0 flow for a specific Google account.
    - Looks for a valid, existing token.
    - If none, launches a browser flow for user consent.
    - Saves the new token for future use.
    Returns authenticated credentials.
    """
    creds = None
    token_path = f"src/credentials/{account_email}.token.json"
    creds_path = f"src/credentials/{account_email}.json"

    # Check if the required credential file exists
    if not os.path.exists(creds_path):
        raise FileNotFoundError(f"Credential file not found for {account_email} at {creds_path}")

    # Check for an existing token file
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            console.print(f"Refreshing token for {account_email}...")
            creds.refresh(Request())
        else:
            console.print(f"No valid token found. Starting authentication flow for {account_email}...")
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(token_path, "w") as token:
            token.write(creds.to_json())
        console.print(f"Token saved for {account_email} at {token_path}")

    return creds

def get_calendar_service(account_email: str):
    """Builds and returns a Google Calendar service client."""
    creds = authenticate_google_account(account_email)
    service = build("calendar", "v3", credentials=creds)
    return service

def get_gmail_service(account_email: str):
    """Builds and returns a Gmail service client."""
    creds = authenticate_google_account(account_email)
    service = build("gmail", "v1", credentials=creds)
    return service

def get_people_service(account_email: str):
    """Builds and returns a Google People API service client."""
    creds = authenticate_google_account(account_email)
    service = build("people", "v1", credentials=creds)
    return service

def get_google_contacts(service):
    """Fetches all Google Contacts with phone numbers."""
    contacts = []
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1000,
        personFields='names,phoneNumbers'
    ).execute()
    
    connections = results.get('connections', [])
    for person in connections:
        names = person.get('names', [])
        phone_numbers = person.get('phoneNumbers', [])
        if names and phone_numbers:
            contacts.append({
                "name": names[0].get('displayName'),
                "number": phone_numbers[0].get('value')
            })
    return contacts

def get_label_map(service):
    """
    Fetches all Gmail labels and returns a dictionary mapping ID to Name.
    """
    label_map = {}
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    for label in labels:
        label_map[label['id']] = label['name']
    return label_map 