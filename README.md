# Igor - Personal AI Assistant

Igor is a command-line based personal AI assistant designed to centralize and automate various aspects of your digital life. It provides a unified interface to interact with services like Notion, Google Calendar, and more.

## ✨ Features

-   **Notion Integration:**
    -   Log application events and other data directly to a Notion database.
-   **Google Calendar Integration:**
    -   Securely authenticate with your Google account using OAuth 2.0.
    -   List upcoming events from your primary calendar.
-   **Extensible CLI:**
    -   Built with Typer, making it easy to add new commands and functionality.
-   **Secure Credential Management:**
    -   Handles API keys and OAuth tokens securely, without hardcoding them.

## 🚀 Getting Started

### Prerequisites

-   Python 3.10+
-   A Notion account and an Internal Integration Token.
-   A Google Cloud Platform account.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd Igor
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv src/venv
    source src/venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r src/requirements.txt
    ```

4.  **Configure Credentials:**
    -   **Notion:**
        -   Copy `src/example.env` to `src/.env`.
        -   Add your Notion API Key and the Log Database ID to the `.env` file.
    -   **Google:**
        -   Follow the Google Cloud setup guide in the `memory_bank` to get your `credentials.json`.
        -   Place the file in `src/credentials/your.email@gmail.com.json`.

## 💻 Usage

The application is run via the `main.py` script. Here are some of the available commands:

```bash
# Display all available commands
python3 src/main.py --help

# Log a message to your Notion database
python3 src/main.py log --message "This is a test log entry."

# Authenticate a Google Account (first time only)
python3 src/main.py calendar-auth --account "your.email@gmail.com"

# List today's calendar events
python3 src/main.py calendar-today --account "your.email@gmail.com"
``` 