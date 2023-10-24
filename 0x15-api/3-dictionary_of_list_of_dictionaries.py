#!/usr/bin/python3
import sys
import requests
import json

# Define the base URL of the API
base_url = "https://jsonplaceholder.typicode.com"

# Get a list of all user IDs
user_ids = range(1, 11)  # Assuming user IDs from 1 to 10

# Create a dictionary to store tasks for all employees
all_employee_tasks = {}

# Loop through all employee IDs
for employee_id in user_ids:
    # Define the API endpoint for user's TODO list
    todo_endpoint = f"{base_url}/todos?userId={employee_id}"

    # Make a GET request to get the user's TODO list
    response = requests.get(todo_endpoint)

    # Check if the TODO list was retrieved successfully
    if response.status_code == 200:
        # Parse the TODO list
        todo_list = response.json()

        # Get the employee's name
        user_endpoint = f"{base_url}/users/{employee_id}"
        user_response = requests.get(user_endpoint)
        user_data = user_response.json()
        user_name = user_data["name"]

        # Add tasks to the dictionary
        all_employee_tasks[employee_id] = [
            {
                "username": user_name,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todo_list
        ]

# Create a JSON file containing tasks for all employees
json_filename = "todo_all_employees.json"

# Write the JSON data to the file
with open(json_filename, 'w') as json_file:
    json.dump(all_employee_tasks, json_file, indent=4)

print(f"Data for all employees exported to {json_filename}.")

