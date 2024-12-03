import json
from datetime import datetime
from collections import Counter
from rich.console import Console
from rich.table import Table
from rich.text import Text
import pyfiglet

# Initialize rich console
console = Console()

# Load data from the JSON file
file_path = "strava_2024_activities.json"  # Adjust this if your file is elsewhere
with open(file_path, "r") as file:
    activities = json.load(file)

total_activities = 0
total_distance = 0.0
total_time = 0
activity_types = Counter()
days_active = Counter()

for activity in activities:
    # Combine "Workout" and "WeightTraining" into "Workout"
    activity_type = activity["type"]
    if activity_type in ["Workout", "WeightTraining"]:
        activity_type = "Workout"

    total_activities += 1
    total_distance += activity.get("distance", 0)  
    total_time += activity.get("moving_time", 0) 
    activity_types[activity_type] += 1

    # Extract day of the week 
    start_date = activity["start_date"]
    date_obj = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ") 
    days_active[date_obj.strftime("%A")] += 1

# Convert total distance to kilometers and total time to hours
total_distance_km = total_distance / 1000
total_time_hours = total_time / 3600

# Find most frequent activity type and most active day
most_common_activity = activity_types.most_common(1)[0]
most_active_day = max(days_active.items(), key=lambda x: x[1] if x[1] > 1 else -1)

# Display ASCII title
ascii_title = pyfiglet.figlet_format("Strava Summary 2024")
console.print(f"[bold magenta]{ascii_title}[/bold magenta]")

table = Table(title="📊 Your 2024 Strava Summary 📊", title_style="bold yellow")

table.add_column("Metric", style="cyan", no_wrap=True)
table.add_column("Value", style="green", justify="right")

table.add_row("Total Activities", f"{total_activities}")
table.add_row("Total Distance", f"{total_distance_km:.2f} km")
table.add_row("Total Time Spent", f"{total_time_hours:.2f} hours")
table.add_row("Most Frequent Activity", f"{most_common_activity[0]} ({most_common_activity[1]} times)")
if most_active_day[1] > 1: 
    table.add_row("Most Active Day", f"{most_active_day[0]} ({most_active_day[1]} activities)")
else:
    table.add_row("Most Active Day", "No significant activity day")

console.print(table)

console.print("\n🗓️ [bold blue]Activity Breakdown by Type:[/bold blue]")
for activity_type, count in activity_types.items():
    console.print(f"- [bold cyan]{activity_type}[/bold cyan]: [green]{count}[/green]")

console.print("\n[bold magenta]Keep up the great work and crush your 2024 goals! 🚀💪[/bold magenta]")
