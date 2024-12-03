import os
import requests
import time
from datetime import datetime
import json
import webbrowser
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

client_id = os.getenv('STRAVA_CLIENT_ID')
client_secret = os.getenv('STRAVA_CLIENT_SECRET')
redirect_uri = os.getenv('STRAVA_REDIRECT_URL')

if not client_id or not client_secret or not redirect_uri:
    raise ValueError("Missing STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET, or STRAVA_REDIRECT_URL in .env file.")

scope = 'activity:read_all'

def main():
    # Obtain authorization code
    auth_url = f'http://www.strava.com/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&approval_prompt=force&scope={scope}'
    print(f'Please go to this URL and authorize the application: {auth_url}')
    webbrowser.open(auth_url)
    code = input('Enter the authorization code from the URL: ')

    # Exchange authorization code for access token
    token_response = requests.post(
        url='https://www.strava.com/oauth/token',
        data={
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'grant_type': 'authorization_code'
        }
    )
    token_response_data = token_response.json()
    access_token = token_response_data.get('access_token')

    if not access_token:
        print("Failed to obtain access token. Response:", token_response_data)
        return

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31, 23, 59, 59)
    after = int(time.mktime(start_date.timetuple()))
    before = int(time.mktime(end_date.timetuple()))

    # Fetch activities
    headers = {'Authorization': f'Bearer {access_token}'}
    activities_url = 'https://www.strava.com/api/v3/athlete/activities'
    activities = []
    page = 1
    per_page = 30  # Number of activities per page

    while True:
        params = {
            'before': before,
            'after': after,
            'page': page,
            'per_page': per_page
        }
        response = requests.get(activities_url, headers=headers, params=params)
        data = response.json()

        if not data:
            break

        activities.extend(data)
        page += 1

    #Save the data
    with open('strava_2024_activities.json', 'w') as f:
        json.dump(activities, f, indent=4)

    print('Data saved to strava_2024_activities.json')

if __name__ == "__main__":
    main()
