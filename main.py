import requests

# Define only the minimal required cookies for the API call
cookies = {
    'session_id': 'your_session_cookie_value',
    # Uncomment and add other cookies if needed, e.g., 'csrf_token': 'your_csrf_token'
}

# Replace with your API endpoint
api_url = 'https://api.example.com/data'

try:
    response = requests.get(api_url, cookies=cookies)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    data = response.json()
    print("API Response:")
    print(data)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
