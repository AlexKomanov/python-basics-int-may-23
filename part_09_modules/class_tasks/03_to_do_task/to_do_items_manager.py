# Task Manager Program

# Initialize an empty list to store tasks
tasks = []


# Function to display the menu
def display_menu():
    print("Task Manager Menu:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


# Function to add a new task
def add_task():
    task_description = input("Enter the task description: ")
    tasks.append({"description": task_description, "completed": False})
    print("Task added!")


# Function to view all tasks
def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = " (Completed)" if task["completed"] else ""
        print(f"{i}. {task['description']}{status}")


# Function to mark a task as completed
def mark_completed():
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


# Function to delete a task
def delete_task():
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task['description']}' deleted!")
    else:
        print("Invalid task number.")


# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the Task Manager.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4/5).")
