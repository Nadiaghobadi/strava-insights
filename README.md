# Strava Insights 🚴‍♂️📊

** Strava Insights ** is a Python project designed to extract, analyze, and visualize your Strava activity data. It provides detailed insights into your workouts, and progress throughout the year with monthly activity visualizations.

---

## Prerequisites 

Make sure you have:
- **Python 3.8 or higher**
- Required libraries:

  ```pip install requests matplotlib rich pyfiglet```


- A Strava developer account for API credentials:
    - Go to Strava Developers.
    - Create an app and note your client_id and client_secret

## Steps:
1. Create a .env file in the project directory and add the following:
```
STRAVA_CLIENT_ID=<your_client_id>
STRAVA_CLIENT_SECRET=<your_client_secret>
STRAVA_REDIRECT_URL=http://localhost/exchange_token
```
Run the following to fetch data from Strava API and save it to a JSON file.
```
python extract_strava_data.py

```
The extract_strava_data.py script fetches data from the Strava API and saves it to a JSON file.
2. Generate Insights:
Run the following:
```
python insights.py
```
3. Visualize Monthly acitivity data:
```
python visualize_strava.py
```