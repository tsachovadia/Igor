import typer
from rich.console import Console
import config
from clients import notion as nc
from clients import google_client as gc
from clients import whatsapp_client as wc
from clients import filesystem_client as fc
import llm_agent as agent
import system_mapper as sm
import report_generator as rg
import datetime
import re
import os

app = typer.Typer()
console = Console()

# Create organizer subcommand group
organizer_app = typer.Typer()
app.add_typer(organizer_app, name="organizer", help="Commands for filesystem analysis and organization using PARA method.")

@organizer_app.command(name="audit")
def run_system_audit(
    output_dir: str = typer.Option(".", "--output", "-o", help="Directory to save the generated reports."),
    max_depth: int = typer.Option(6, "--depth", "-d", help="Maximum directory depth to scan.")
):
    """
    Scans the filesystem, maps applications, and generates a full PARA-method audit.
    """
    console.print("[bold blue]🔍 Starting Igor System Audit...[/bold blue]")
    
    try:
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Step 1: Scan filesystem
        console.print("\n[bold yellow]📁 Step 1: Scanning filesystem...[/bold yellow]")
        filesystem_data = fc.scan_filesystem_bfs(max_depth=max_depth)
        console.print("[green]✓ Filesystem scan completed.[/green]")
        
        # Step 2: Map applications
        console.print("\n[bold yellow]🖥️  Step 2: Mapping system applications...[/bold yellow]")
        applications_data = sm.map_system_applications()
        console.print("[green]✓ Application mapping completed.[/green]")
        
        # Step 3: Generate reports
        console.print("\n[bold yellow]📊 Step 3: Generating reports...[/bold yellow]")
        
        # Generate all report files
        database_path = os.path.join(output_dir, "database.json")
        interactive_map_path = os.path.join(output_dir, "interactive_map.html")
        editable_map_path = os.path.join(output_dir, "editable_map.md")
        markdown_report_path = os.path.join(output_dir, "system_report.md")
        
        rg.generate_json_database(filesystem_data, applications_data, database_path)
        rg.generate_interactive_map(filesystem_data, interactive_map_path)
        rg.generate_editable_map(filesystem_data, editable_map_path)
        rg.generate_markdown_report(filesystem_data, applications_data, markdown_report_path)
        
        console.print("[green]✓ All reports generated successfully.[/green]")
        
        # Step 4: Summary
        console.print(f"\n[bold green]🎉 Igor System Audit Complete![/bold green]")
        console.print(f"\n[bold]Generated Files:[/bold]")
        console.print(f"  📄 JSON Database: {database_path}")
        console.print(f"  🌐 Interactive Map: {interactive_map_path}")
        console.print(f"  ✏️  Editable Map: {editable_map_path}")
        console.print(f"  📋 System Report: {markdown_report_path}")
        
        console.print(f"\n[bold cyan]💡 Next Steps:[/bold cyan]")
        console.print(f"  • Open {interactive_map_path} in your browser for interactive exploration")
        console.print(f"  • Review {markdown_report_path} for PARA method recommendations")
        console.print(f"  • Use {editable_map_path} in your favorite mind-mapping tool")
        
    except Exception as e:
        console.print(f"[bold red]❌ Audit failed: {e}[/bold red]")
        raise typer.Exit(1)

@app.command()
def hello():
    """
    Greets the application by its configured name.
    """
    console.print(f"Hello, I am [bold green]{config.APP_NAME}[/bold green]")

@app.command()
def goodbye(name: str, formal: bool = False):
    """
    Says goodbye to the given name.
    """
    if formal:
        console.print(f"Goodbye, {name}. Have a good day.")
    else:
        console.print(f"Later, {name}!")

@app.command(name="notion-check")
def notion_check():
    """
    Verifies the connection to Notion and searches for the 'Igor' database.
    """
    console.print("Attempting to connect to Notion...")
    try:
        client = nc.get_notion_client()
        console.print("[green]✓ Notion client initialized successfully.[/green]")
        
        console.print("Searching for 'Igor' database...")
        results = nc.search_database(client, "Igor")
        
        if not results:
            console.print("[yellow]! Could not find a database named 'Igor'.[/yellow]")
            console.print("Please ensure the database exists and the integration has access to it.")
            return

        console.print(f"[green]✓ Found {len(results)} database(s) named 'Igor':[/green]")
        for db in results:
            db_id = db.get('id')
            db_title = db.get('title', [{}])[0].get('text', {}).get('content', 'No Title')
            console.print(f"  - Title: {db_title}, ID: {db_id}")

    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]An unexpected error occurred: {e}[/red]")

@app.command()
def log(message: str, status: str = "SUCCESS"):
    """
    Creates a log entry in the Notion 'Igor App Logs' database.
    """
    console.print(f"Logging message to Notion: '{message}'")
    try:
        client = nc.get_notion_client()
        db_id = config.IGOR_LOG_DB_ID
        if not db_id:
            raise ValueError("IGOR_LOG_DB_ID is not set in your .env file.")
            
        nc.create_log_entry(
            client=client,
            db_id=db_id,
            title=message,
            command="log",
            status=status.upper(),
            details=f"CLI log entry: {message}"
        )
        console.print("[green]✓ Successfully created log entry in Notion.[/green]")

    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]An unexpected error occurred: {e}[/red]")

@app.command(name="calendar-auth")
def calendar_auth(account: str = typer.Option(..., "--account", "-a", help="The Google account email to authenticate.")):
    """
    Authenticates a Google account and saves the token.
    """
    console.print(f"Starting authentication for [bold]{account}[/bold]...")
    try:
        creds = gc.authenticate_google_account(account)
        if creds:
            console.print(f"[green]✓ Successfully authenticated {account}.[/green]")
            console.print("Token is now stored for future use.")
        else:
            console.print(f"[red]Authentication failed for {account}.[/red]")
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
        console.print("Please ensure the credential file exists and is named correctly (e.g., src/credentials/your.email@gmail.com.json).")
    except Exception as e:
        console.print(f"[red]An unexpected error occurred during authentication: {e}[/red]")

@app.command(name="calendar-today")
def calendar_today(account: str = typer.Option(..., "--account", "-a", help="The Google account email to use.")):
    """
    Lists today's events from the specified Google Calendar.
    """
    console.print(f"Fetching today's events for [bold]{account}[/bold]...")
    try:
        service = gc.get_calendar_service(account)
        
        # Get the start and end of today
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        events_result = service.events().list(
            calendarId='primary', 
            timeMin=now,
            maxResults=10, 
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])

        if not events:
            console.print("No upcoming events found for today.")
            return

        console.print("[bold green]Today's Events:[/bold green]")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            console.print(f"- {start}: {event['summary']}")

    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")

@app.command(name="gmail-labels")
def gmail_labels(
    account: str = typer.Option(..., "--account", "-a", help="The Google account email to use."),
    custom_only: bool = typer.Option(False, "--custom-only", help="Show only custom, user-created labels.")
):
    """
    Lists all available labels from the specified Gmail account.
    """
    console.print(f"Fetching labels for [bold]{account}[/bold]...")
    try:
        service = gc.get_gmail_service(account)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            console.print("No labels found.")
            return

        console.print("[bold green]Available Gmail Labels:[/bold green]")
        for label in labels:
            if custom_only and not label['id'].startswith('Label_'):
                continue
            console.print(f"- {label['name']} (ID: {label['id']})")

    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")

@app.command(name="gmail-fetch")
def gmail_fetch(
    account: str = typer.Option(..., "--account", "-a", help="The Google account email to use."),
    label: str = typer.Option("INBOX", "--label", "-l", help="The label to fetch emails from."),
    limit: int = typer.Option(5, "--limit", "-n", help="The number of emails to fetch.")
):
    """
    Fetches a limited number of recent emails from a specific label.
    """
    console.print(f"Fetching {limit} emails from label '{label}' for [bold]{account}[/bold]...")
    try:
        service = gc.get_gmail_service(account)
        
        console.print("Fetching label map...")
        label_map = gc.get_label_map(service)
        console.print("✓ Label map fetched.")

        # List messages with the specified label
        results = service.users().messages().list(userId='me', labelIds=[label], maxResults=limit).execute()
        messages = results.get('messages', [])

        if not messages:
            console.print(f"No messages found in label '{label}'.")
            return

        console.print(f"[bold green]Found {len(messages)} messages:[/bold green]")
        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
            payload = msg_data.get('payload', {})
            headers = payload.get('headers', [])
            
            subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), 'No Subject')
            from_email = next((h['value'] for h in headers if h['name'].lower() == 'from'), 'No Sender')
            date_str = next((h['value'] for h in headers if h['name'].lower() == 'date'), '')

            # Parse the date
            # We need to handle different date formats from Gmail
            try:
                # Example: 'Tue, 17 Jun 2025 17:29:10 +0000'
                parsed_date = datetime.datetime.strptime(date_str.split(' (')[0].strip(), '%a, %d %b %Y %H:%M:%S %z')
                iso_date = parsed_date.isoformat()
            except ValueError:
                iso_date = datetime.datetime.now(datetime.timezone.utc).isoformat()

            # Translate label IDs to names
            label_ids = msg_data.get('labelIds', [])
            label_names = [label_map.get(lid, lid) for lid in label_ids]

            email_data = {
                "subject": subject,
                "from_email": from_email,
                "date": iso_date,
                "snippet": msg_data.get('snippet', ''),
                "account": account,
                "message_id": msg['id'],
                "labels": label_names,
            }

            # Add to Notion
            notion_client = nc.get_notion_client()
            gmail_db_id = config.GMAIL_DB_ID
            if not gmail_db_id:
                raise ValueError("GMAIL_DB_ID is not set in your .env file.")
            
            # Check for duplicates before adding
            if nc.check_if_email_exists(notion_client, gmail_db_id, email_data["message_id"]):
                console.print(f"  - Skipping '{subject}' (already exists in Notion).")
                continue

            nc.add_email_to_notion(notion_client, gmail_db_id, email_data)
            console.print(f"  > Added '{subject}' to Notion.")

    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")

@app.command()
def chat(account: str = typer.Option(..., "--account", "-a", help="The Google account email to use for the session.")):
    """
    Starts an interactive chat session with the Igor AI agent.
    """
    console.print("[bold]Initializing Igor's Brain...[/bold]")
    try:
        # 1. Gather all context
        console.print("  > Loading Notion client...")
        notion_client = nc.get_notion_client()
        
        console.print("  > Loading Google client...")
        google_service = gc.get_gmail_service(account)
        
        console.print("  > Fetching Notion projects...")
        projects_db_id = config.UB_PROJECTS_DB_ID
        if not projects_db_id:
            raise ValueError("UB_PROJECTS_DB_ID is not set.")
        project_names = nc.get_projects_from_ub(notion_client, projects_db_id)
        
        console.print("  > Fetching Gmail labels...")
        label_map = gc.get_label_map(google_service)
        custom_labels = [name for lid, name in label_map.items() if lid.startswith("Label_")]

        initial_context = {
            "projects": project_names,
            "labels": custom_labels,
            "account": account,
        }
        
        console.print("[green]Initialization complete.[/green]")
        
        # 2. Start the interactive session
        agent.start_chat_session(initial_context)

    except Exception as e:
        console.print(f"[bold red]Initialization Failed: {e}[/bold red]")

@app.command(name="gemini-test")
def gemini_test():
    """
    Sends a simple, direct test prompt to the Gemini API to verify the connection and quota.
    """
    console.print("Sending a simple test prompt to Gemini...")
    try:
        model = agent.get_generative_model()
        response = model.generate_content("What is the speed of light?")
        console.print("[bold green]✓ Test successful![/bold green]")
        console.print(f"Gemini's response: {response.text}")
    except Exception as e:
        console.print(f"[bold red]Test failed. The issue is likely with your API key or billing setup.[/bold red]")
        console.print(f"Error details: {e}")

@app.command(name="whatsapp-send")
def whatsapp_send(
    to: str = typer.Option(..., "--to", help="The recipient's phone number in the format 79991234567."),
    message: str = typer.Option(..., "--message", "-m", help="The message to send.")
):
    """Sends a WhatsApp message via Green-API."""
    console.print(f"Sending WhatsApp message to [bold]{to}[/bold]...")
    try:
        client = wc.get_whatsapp_client()
        response = wc.send_whatsapp_message(client, to, message)
        
        if response.code == 200 and response.data.get('idMessage'):
            console.print(f"[green]✓ Message sent successfully![/green]")
            console.print(f"  Message ID: {response.data['idMessage']}")
        else:
            console.print(f"[red]Error sending message.[/red]")
            console.print(f"  Response: {response.error}")

    except Exception as e:
        console.print(f"[red]An unexpected error occurred: {e}[/red]")

@app.command(name="whatsapp-status")
def whatsapp_status():
    """Checks the connection status of the WhatsApp instance via Green-API."""
    console.print("Checking WhatsApp instance status...")
    try:
        client = wc.get_whatsapp_client()
        response = wc.get_instance_state(client)
        
        if response.code == 200:
            state = response.data.get("stateInstance")
            console.print(f"[green]✓ Connection successful![/green]")
            console.print(f"  Instance State: [bold]{state}[/bold]")
            if state == "authorized":
                console.print("  [green]Your account is connected and ready.[/green]")
            else:
                console.print("  [yellow]Your account is not authorized. Please check your Green-API dashboard and scan the QR code.[/yellow]")
        else:
            console.print(f"[red]Error checking status.[/red]")
            console.print(f"  Response: {response.error}")

    except Exception as e:
        console.print(f"[red]An unexpected error occurred: {e}[/red]")

@app.command(name="whatsapp-configure")
def whatsapp_configure(delay: int = typer.Option(1000, "--delay", help="The delay in milliseconds between sent messages.")):
    """Sets key instance settings for message journaling and safety."""
    console.print(f"Applying optimal instance settings (with a {delay}ms delay)...")
    try:
        settings = {
            "delaySendMessagesMilliseconds": delay,
            "incomingWebhook": "yes",
            "outgoingMessageWebhook": "yes",
            "stateWebhook": "yes"
        }
        client = wc.get_whatsapp_client()
        response = wc.update_instance_settings(client, settings)
        
        if response.code == 200 and response.data.get("saveSettings"):
            console.print(f"[green]✓ Settings updated successfully.[/green]")
        else:
            console.print(f"[red]Error updating settings.[/red]")
            console.print(f"  Response: {response.error}")

    except Exception as e:
        console.print(f"[red]An unexpected error occurred: {e}[/red]")

@app.command(name="sync-contacts")
def sync_contacts(account: str = typer.Option(..., "--account", "-a", help="The Google account to sync contacts from.")):
    """
    Intelligently syncs contacts from Google and WhatsApp to a central Notion database.
    """
    console.print("Starting intelligent contact sync...")
    try:
        # Initialize clients
        notion_client = nc.get_notion_client()
        wa_client = wc.get_whatsapp_client()
        people_service = gc.get_people_service(account)

        contacts_db_id = config.WHATSAPP_CONTACTS_DB_ID
        if not contacts_db_id:
            raise ValueError("WHATSAPP_CONTACTS_DB_ID is not set.")

        # 1. Fetch Google Contacts (The "Source of Truth" for names)
        console.print("Fetching contacts from Google...")
        google_contacts = gc.get_google_contacts(people_service)
        google_contact_map = {
            # Normalize phone numbers for matching
            re.sub(r'\D', '', c.get('number', '')): c.get('name') 
            for c in google_contacts if c.get('number')
        }
        console.print(f"✓ Found {len(google_contact_map)} named contacts in Google.")

        # 2. Fetch all WhatsApp chats
        console.print("Fetching contacts from WhatsApp...")
        wa_contacts = wc.get_contacts(wa_client).data
        console.print(f"✓ Found {len(wa_contacts)} total WhatsApp entries.")

        # 3. Process and Sync
        console.print("Filtering, merging, and syncing to Notion...")
        for contact in wa_contacts:
            contact_id = contact.get("id", "")
            wa_name = contact.get("name", "")
            
            if not contact_id: continue

            number = contact_id.split('@')[0]
            
            # Skip if contact already exists in Notion
            if nc.check_if_contact_exists(notion_client, contacts_db_id, number):
                continue
            
            final_name = ""
            status = ""
            source = ""
            kind = ""

            if contact_id.endswith("@c.us"):
                kind = "Person"
                # Check if this number exists in our Google contacts map
                clean_number = re.sub(r'\D', '', number)
                if google_contact_map.get(clean_number):
                    final_name = google_contact_map[clean_number]
                    status = "Saved"
                    source = "Google Contacts"
                else:
                    final_name = number # Use number as name for unsaved
                    status = "Unsaved"
                    source = "WhatsApp Only"
            
            elif contact_id.endswith("@g.us"):
                if not wa_name: continue # Skip groups without a name
                kind = "Group"
                final_name = wa_name
                status = "Saved"
                source = "WhatsApp Only"
            
            else:
                continue # Skip non-person/group chats

            contact_data = {
                "name": final_name,
                "number": number,
                "kind": kind,
                "status": status,
                "source": source
            }
            nc.add_contact_to_notion(notion_client, contacts_db_id, contact_data)
            console.print(f"  > Synced {kind} '{final_name}' from {source}")

        console.print("[green]✓ Intelligent contact sync complete.[/green]")

    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")

@app.command(name="contacts-sync-google")
def contacts_sync_google(account: str = typer.Option(..., "--account", "-a", help="The Google account to sync contacts from.")):
    """
    Syncs all named contacts from Google Contacts to the Notion database.
    """
    console.print(f"Starting Google Contacts sync for [bold]{account}[/bold]...")
    try:
        # Initialize clients
        notion_client = nc.get_notion_client()
        people_service = gc.get_people_service(account)

        contacts_db_id = config.WHATSAPP_CONTACTS_DB_ID
        if not contacts_db_id:
            raise ValueError("WHATSAPP_CONTACTS_DB_ID is not set.")

        # 1. Fetch Google Contacts
        console.print("Fetching contacts from Google...")
        google_contacts = gc.get_google_contacts(people_service)
        console.print(f"✓ Found {len(google_contacts)} named contacts in Google.")

        # 2. Add to Notion, checking for duplicates
        for contact in google_contacts:
            number = contact.get("number")
            if not number:
                continue

            clean_number = re.sub(r'\D', '', number)

            if nc.check_if_contact_exists(notion_client, contacts_db_id, clean_number):
                continue
            
            contact_data = {
                "name": contact.get("name"),
                "number": clean_number,
                "kind": "Person",
                "status": "Saved",
                "source": "Google Contacts"
            }
            nc.add_contact_to_notion(notion_client, contacts_db_id, contact_data)
            console.print(f"  > Synced {contact.get('name')} ({clean_number}) from Google.")

        console.print("[green]✓ Google Contacts sync complete.[/green]")

    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")

if __name__ == "__main__":
    app() 