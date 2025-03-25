# Simple API Client Script

This Python script demonstrates how to make a basic GET request to a specified API endpoint using the `requests` library. It specifically shows how to include essential cookies (like a session ID) with the request, which is often necessary for authentication or maintaining session state with web APIs.

## Features

*   Uses the `requests` library to perform HTTP GET requests.
*   Includes a pre-defined dictionary for necessary cookies (easily configurable).
*   Targets a configurable API endpoint URL.
*   Checks for HTTP errors (status codes 4xx or 5xx) after the request.
*   Parses the JSON response from the API.
*   Prints the received data or an error message if the request fails.
*   Includes basic error handling for network-related issues.

## Prerequisites

*   **Python 3:** Ensure you have Python 3 installed.
*   **requests library:** If you don't have it installed, run:
    ```bash
    pip install requests
    ```

## Setup

Before running the script, you need to configure two main parts:

1.  **Cookies:**
    *   Open the script (`main.py`, replace with the actual filename).
    *   Locate the `cookies` dictionary.
    *   Replace `'your_session_cookie_value'` with your actual session ID cookie value. You can typically find this using your browser's developer tools (look under Application -> Cookies for the relevant domain).
    *   If the API requires other cookies (like a CSRF token), uncomment and add them to the `cookies` dictionary as needed.

    ```python
    # Define only the minimal required cookies for the API call
    cookies = {
        'session_id': 'your_session_cookie_value', # <-- REPLACE THIS VALUE
        # Uncomment and add other cookies if needed, e.g., 'csrf_token': 'your_csrf_token'
    }
    ```

2.  **API Endpoint URL:**
    *   In the same script, find the `api_url` variable.
    *   Replace `'https://api.example.com/data'` with the actual URL of the API endpoint you want to query.

    ```python
    # Replace with your API endpoint
    api_url = 'https://api.example.com/data' # <-- REPLACE THIS URL
    ```

## Usage

Once the script is configured, you can run it from your terminal:

```bash
python main.py