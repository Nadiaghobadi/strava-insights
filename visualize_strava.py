import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter

# Load data from the JSON file
file_path = "strava_2024_activities.json"
    activities = json.load(file)

workout_dates = []
for activity in activities:
    # if activity["type"] in ["Workout", "WeightTraining", "Walk"]:  # Filter by activity type
    start_date = activity["start_date"]
    date_obj = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ")
    workout_dates.append((date_obj.year, date_obj.month))

# Count the number of workouts per month
workout_counts = Counter(workout_dates)

#Add data per month
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_counts = [0] * 12  # Initialize counts for all months

for (year, month), count in workout_counts.items():
    monthly_counts[month - 1] += count

plt.figure(figsize=(10, 6))
plt.bar(months, monthly_counts, alpha=0.7)
plt.title("Number of Workouts per Month (2024)", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Number of Workouts", fontsize=14)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
