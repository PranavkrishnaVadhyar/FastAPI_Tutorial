"""

1. JSON as a Storage Solution
- How to use JSON files as a lightweight and persistent data storage.
- Loading data from and saving data to JSON files.

2. File Operations
- Using Python's `open()` function to read and write files.
- Handling file-related errors, such as `FileNotFoundError`.

3. Utility Functions
- Modularizing reusable functions (`load_tasks`, `save_tasks`) for better code organization.
- Centralized data management for tasks.

Usage in Code
- `load_tasks()` loads tasks from the JSON file, returning them as a list.
- `save_tasks(tasks)` saves the given task list back to the JSON file.


"""

import json

STORAGE_FILE = "C:/Users/bpran/Desktop/FastAPI_Session/FastAPI_Tutorial/app/storage.json"

def load_tasks():
    try:
        with open(STORAGE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(STORAGE_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
