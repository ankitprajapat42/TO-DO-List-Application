# TO-DO List Application

This is a Python-based **TO-DO List Application** that allows users to manage their tasks efficiently. The application provides functionalities to add, update, delete, and view tasks, making it a simple yet effective tool for task management.

## Features
1. **Add Tasks**:
   - Add multiple tasks at once.
   - Appends tasks to the existing list.
2. **Update Tasks**:
   - Modify a specific task by replacing it with a new one.
   - Checks if the task exists in the list before updating.
3. **Delete Tasks**:
   - Remove a specific task from the list.
   - Ensures the task exists before attempting to delete.
4. **View Tasks**:
   - Display all the tasks in the list in sequential order.
5. **Exit**:
   - Exit the application cleanly.

## How It Works
1. The program starts with a menu displayed to the user:
   - Press `1` to add tasks.
   - Press `2` to delete tasks.
   - Press `3` to update tasks.
   - Press `4` to view all tasks.
   - Press `5` to exit.
2. The user selects an option, and the program performs the corresponding operation.
3. The task list (`task`) is dynamically updated based on the user's actions.
4. The application runs in a loop until the user decides to exit.

## Requirements
- Python 3.x (No additional libraries required)

## How to Run
1. Clone the repository or download the script file.
2. Open a terminal or command prompt in the script's directory.
3. Run the script using:
   ```bash
   python todo_list.py
