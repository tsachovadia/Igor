# Project Tasks

This file tracks the development tasks for the Igor project.

## Phase 1: Foundation & Core Functionality

-   [x] Create project directory and Memory Bank structure.
-   [x] Define `projectbrief.md` and `techContext.md`.
-   [x] Initialize Python project (`main.py`, `requirements.txt`, `.gitignore`).
-   [x] Build the basic Command-Line Interface (CLI) framework.
-   [x] Implement secure handling for API keys and environment variables.

## Phase 2: Notion Integration

-   [x] Develop `notion.py` for API communication.
-   [x] Implement functions to search for databases and pages.
-   [x] Add `notion-check` CLI command.
-   [x] Design and create the `Igor App Logs` database in Notion.
-   [x] Implement `log` command to write to the Notion database.

## Phase 3: Google Calendar Integration

-   [x] Guide user through creating Google Cloud credentials (`credentials.json`) for one account.
-   [x] Add Google API libraries to `requirements.txt`.
-   [x] Develop `google_client.py` to handle OAuth 2.0 flow and create a service object.
-   [x] Implement function to list calendar events.
-   [x] Add `calendar list-events` command to CLI.

## Phase 4: Expansion & Refinement

-   [x] Begin Gmail integration (e.g., list unread emails).
-   [x] Design and create the `Igor - Gmail Inbox` database in Notion.
-   [x] Implement a pipeline to fetch emails and populate the Notion database.
-   [x] Add inline documentation for the database to the 'Igor' Notion page.
-   [ ] Implement duplicate checking for the email sync.
-   [ ] Integrate additional Google accounts (`itsdrtsach@gmail.com`, `zack@macabi.us`).

## Future Phases

-   [ ] Expand Notion integration (e.g., read/write to task database).
-   [ ] Investigate and integrate WhatsApp.
-   [ ] Develop AI analysis modules. 