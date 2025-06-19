import notion_client
import config

def get_notion_client():
    """Initializes and returns the Notion client."""
    if not config.NOTION_API_KEY:
        raise ValueError("NOTION_API_KEY environment variable not set.")
    
    return notion_client.Client(auth=config.NOTION_API_KEY)

def search_database(client: "notion_client.Client", query: str):
    """Searches for a database by its title."""
    response = client.search(query=query, filter={"value": "database", "property": "object"})
    return response.get("results")

def create_log_entry(client: "notion_client.Client", db_id: str, title: str, command: str, status: str, details: str):
    """Creates a new page (log entry) in the specified database."""
    properties = {
        "'Log Entry'": {"title": [{"text": {"content": title}}]},
        "Command": {"rich_text": [{"text": {"content": command}}]},
        "Status": {"select": {"name": status}},
        "Details": {"rich_text": [{"text": {"content": details}}]},
    }
    
    return client.pages.create(parent={"database_id": db_id}, properties=properties)

def add_email_to_notion(client: "notion_client.Client", db_id: str, email_data: dict):
    """
    Adds a new email to the specified Notion database.
    Uses the quoted property names as a workaround for the API bug.
    """
    properties = {
        "'Subject'": {"title": [{"text": {"content": email_data.get("subject", "No Subject")}}]},
        "'From'": {"email": email_data.get("from_email")},
        "'Date'": {"date": {"start": email_data.get("date")}},
        "'Snippet'": {"rich_text": [{"text": {"content": email_data.get("snippet", "")}}]},
        "'Account'": {"select": {"name": email_data.get("account")}},
        "'Message-ID'": {"rich_text": [{"text": {"content": email_data.get("message_id")}}]},
        "'Status'": {"select": {"name": "New"}},
        "'Gmail Labels'": {"multi_select": [{"name": label} for label in email_data.get("labels", [])]},
    }
    
    return client.pages.create(parent={"database_id": db_id}, properties=properties)

def check_if_email_exists(client: "notion_client.Client", db_id: str, message_id: str):
    """
    Queries the Notion database to see if an email with the given Message-ID already exists.
    Returns True if it exists, False otherwise.
    """
    results = client.databases.query(
        database_id=db_id,
        filter={
            "property": "'Message-ID'",
            "rich_text": {
                "equals": message_id
            }
        }
    )
    return len(results.get("results", [])) > 0

def add_contact_to_notion(client: "notion_client.Client", db_id: str, contact_data: dict):
    """Adds a new contact to the specified Notion database."""
    properties = {
        "Name": {"title": [{"text": {"content": contact_data.get("name", "Unknown")}}]},
        "Number": {"phone_number": contact_data.get("number")},
        "Contact Kind": {"select": {"name": contact_data.get("kind")}},
        "Status": {"select": {"name": contact_data.get("status")}},
        "Source": {"select": {"name": contact_data.get("source")}},
        "Type": {"select": {"name": "Personal"}}, # Defaulting to personal for now
    }
    return client.pages.create(parent={"database_id": db_id}, properties=properties)

def check_if_contact_exists(client: "notion_client.Client", db_id: str, phone_number: str):
    """
    Queries the Notion contacts database to see if a contact with the given phone number already exists.
    Returns True if it exists, False otherwise.
    """
    results = client.databases.query(
        database_id=db_id,
        filter={
            "property": "Number",
            "phone_number": {
                "equals": phone_number
            }
        }
    )
    return len(results.get("results", [])) > 0

def get_projects_from_ub(client: "notion_client.Client", db_id: str):
    """
    Fetches all pages from the 'Projects [UB]' database and returns a list of project names.
    """
    project_names = []
    results = client.databases.query(
        database_id=db_id,
        filter={
            "property": "Status",
            "status": {
                "does_not_equal": "Done"
            }
        }
    ).get("results", [])

    for page in results:
        properties = page.get("properties", {})
        name_property = properties.get("Name", {})
        title_list = name_property.get("title", [])
        if title_list:
            project_names.append(title_list[0].get("plain_text", ""))
    
    return project_names 