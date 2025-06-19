import google.generativeai as genai
import config
from rich.console import Console
import json
from clients import google_client as gc # Import our google client

console = Console()

def configure_llm():
    """Configures the Gemini API with the key."""
    if not config.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set in your .env file.")
    genai.configure(api_key=config.GEMINI_API_KEY)

def get_generative_model():
    """Returns a configured Gemini Pro model instance."""
    configure_llm()
    # For now, we use the base model. Later, we can add system instructions here.
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    return model

def build_master_prompt(context: dict, email_body: str):
    """Builds the master prompt with all the context for the LLM."""

    # We can add more context sections here later (e.g., calendar events)
    prompt = f"""
    **System Persona:**
    You are Igor, a highly efficient AI assistant. Your goal is to help the user by analyzing information and suggesting concrete actions. You are concise and focus on actionable outcomes.

    **Context: User's Projects**
    The user is currently working on the following projects:
    {', '.join(context.get('projects', []))}

    **Context: User's Email Labels**
    The user has the following custom email labels:
    {', '.join(context.get('labels', []))}

    **User Request: Analyze Email**
    Analyze the following email and provide a structured summary and recommendations.
    
    **Email Body:**
    ---
    {email_body}
    ---

    **Output Format:**
    Provide your response ONLY in the following JSON format. Do not include any other text or markdown formatting.
    {{
        "summary": "A brief, one-sentence summary of the email's content.",
        "sentiment": "Positive, Negative, or Neutral.",
        "suggested_labels": ["label1", "label2"],
        "suggested_project": "The single most relevant project name from the context, or null.",
        "suggested_action": "A brief, actionable next step for the user (e.g., 'Draft a reply confirming the meeting')."
    }}
    """
    return prompt

def start_chat_session(initial_context: dict):
    """Starts and manages the interactive chat session."""
    model = get_generative_model()
    chat = model.start_chat(history=[])
    console.print("[bold green]Welcome to Igor Chat![/bold green]")
    console.print("Type 'analyze <email_id>' to start, or 'quit' to exit.")

    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            break
        
        if user_input.lower().startswith("analyze "):
            try:
                email_id = user_input.split(" ", 1)[1]
                console.print(f"[italic]Fetching email {email_id}...[/italic]")

                # 1. Fetch the email body
                gservice = gc.get_gmail_service(initial_context['account'])
                msg_data = gservice.users().messages().get(userId='me', id=email_id, format='full').execute()
                
                email_body = ""
                if 'parts' in msg_data['payload']:
                    for part in msg_data['payload']['parts']:
                        if part['mimeType'] == 'text/plain':
                            import base64
                            email_body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                            break
                if not email_body:
                     email_body = msg_data.get('snippet', '') # Fallback to snippet

                # 2. Build the prompt
                prompt = build_master_prompt(initial_context, email_body)
                
                # 3. Send to Gemini
                console.print("[italic]Sending to Gemini for analysis...[/italic]")
                response = chat.send_message(prompt)

                # 4. Parse and display the response
                cleaned_response = response.text.strip().replace("`", "")
                if cleaned_response.startswith("json"):
                    cleaned_response = cleaned_response[4:]

                analysis = json.loads(cleaned_response)

                console.print("\n[bold green]🧠 Igor's Analysis:[/bold green]")
                console.print(f"  [bold]Summary:[/] {analysis.get('summary')}")
                console.print(f"  [bold]Sentiment:[/] {analysis.get('sentiment')}")
                console.print(f"  [bold]Suggested Labels:[/] {', '.join(analysis.get('suggested_labels', []))}")
                console.print(f"  [bold]Suggested Project:[/] {analysis.get('suggested_project', 'None')}")
                console.print(f"  [bold]Suggested Action:[/] {analysis.get('suggested_action')}")
                console.print("-" * 20)

            except Exception as e:
                console.print(f"[bold red]An error occurred during analysis: {e}[/bold red]")

        else:
            console.print("Unknown command. Please use 'analyze <email_id>' or 'quit'.")

# We will add prompt template functions and the chat loop logic here later. 