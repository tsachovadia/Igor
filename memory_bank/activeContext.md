# Active Context

**Current Task:** Develop the Google Calendar client (`google_client.py`).
 
**Goal:** Write the Python code to handle the Google OAuth 2.0 flow using the `credentials.json` file. This involves:
1.  Checking for an existing, valid token.
2.  If no token exists, launching a browser for the user to grant consent.
3.  Saving the new token for future use.
4.  Creating a service object to interact with the Google Calendar API. 