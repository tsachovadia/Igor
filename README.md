# Igor - Personal AI Assistant

Igor is a command-line based personal AI assistant designed to centralize and automate various aspects of your digital life. It provides a unified interface to interact with services like Notion, Google Calendar, WhatsApp, and includes powerful system organization capabilities.

## ✨ Features

-   **System Organization (NEW!):**
    -   **PARA Method Integration:** Analyze and organize your digital environment using the PARA methodology (Projects, Areas, Resources, Archives).
    -   **Filesystem Scanner:** Intelligent BFS-based directory scanning with smart filtering to avoid noise.
    -   **Application Mapper:** Comprehensive mapping of installed applications and plugins.
    -   **Multi-Format Reports:** Generate JSON databases, interactive HTML maps, editable mind maps, and detailed Markdown reports.
-   **Notion Integration:**
    -   Log application events and other data directly to a Notion database.
    -   Sync WhatsApp contacts with intelligent Google Contacts integration.
-   **Google Services Integration:**
    -   **Calendar:** Securely authenticate and list upcoming events.
    -   **Gmail:** Fetch and organize emails with custom label support.
    -   **Contacts:** Sync contacts across platforms with deduplication.
-   **WhatsApp Integration:**
    -   Send messages and check connection status via Green-API.
    -   Intelligent contact synchronization with Google Contacts.
-   **AI-Powered Chat:**
    -   Interactive chat sessions with contextual awareness.
-   **Extensible CLI:**
    -   Built with Typer, making it easy to add new commands and functionality.
-   **Secure Credential Management:**
    -   Handles API keys and OAuth tokens securely, without hardcoding them.

## 🚀 Getting Started

### Prerequisites

-   Python 3.10+
-   A Notion account and an Internal Integration Token.
-   A Google Cloud Platform account.
-   (Optional) WhatsApp Business API via Green-API for messaging features.

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

### 🔍 System Organization Commands

```bash
# Run a complete system audit using PARA methodology
python3 src/main.py organizer audit

# Specify custom output directory and scanning depth
python3 src/main.py organizer audit --output ./reports --depth 4

# View all organizer options
python3 src/main.py organizer --help
```

**Generated Output Files:**
- `database.json` - Complete JSON database with all collected data
- `interactive_map.html` - Interactive mind map (open in browser)
- `editable_map.md` - Markdown mind map for editing in tools like Obsidian
- `system_report.md` - Comprehensive Markdown report with PARA recommendations

### 📝 General Commands

```bash
# Display all available commands
python3 src/main.py --help

# Log a message to your Notion database
python3 src/main.py log --message "This is a test log entry."

# Authenticate a Google Account (first time only)
python3 src/main.py calendar-auth --account "your.email@gmail.com"

# List today's calendar events
python3 src/main.py calendar-today --account "your.email@gmail.com"

# Sync contacts intelligently across platforms
python3 src/main.py sync-contacts --account "your.email@gmail.com"

# Send WhatsApp messages
python3 src/main.py whatsapp-send --to "1234567890" --message "Hello!"

# Start an AI chat session
python3 src/main.py chat --account "your.email@gmail.com"
```

## 🗂️ PARA Method Integration

Igor's Organizer feature helps you implement the **PARA Method** for digital organization:

- **Projects:** Active work requiring attention
- **Areas:** Ongoing responsibilities to maintain  
- **Resources:** Future reference materials
- **Archive:** Inactive items from other categories

The system audit provides specific recommendations for organizing your files and applications according to these principles.

## 📊 System Analysis Features

### Intelligent Filesystem Scanning
- **BFS Algorithm:** Breadth-first search for efficient directory traversal
- **Smart Filtering:** Automatically skips system directories, caches, and noise
- **Progress Tracking:** Visual progress bars for long-running scans
- **Configurable Depth:** Control how deep the scan goes

### Application & Plugin Mapping
- **System Profiler Integration:** Uses macOS `system_profiler` for comprehensive app data
- **Plugin Discovery:** Scans known plugin directories for completeness
- **Usage Analytics:** Tracks last modified dates for usage insights
- **Cross-Platform Ready:** Extensible architecture for other operating systems

### Multi-Format Reporting
- **JSON Database:** Machine-readable complete dataset
- **Interactive Maps:** Browser-based exploration with zoom/pan
- **Editable Maps:** Import into your favorite mind-mapping tools
- **Markdown Reports:** Human-readable analysis with actionable recommendations 