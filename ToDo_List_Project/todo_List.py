import datetime

# tasks array defined globally to fix scope issues
tasks = []

# Define a function to display the list of tasks
def display_tasks():
    if not tasks:
        print("No tasks added yet!\n")
        return

    print("To-Do List:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']} - {task['description']} - {task['due_date']} - {task['status']}")
    print("\n")

# Define a function to add a new task
def add_task():
    while True:
        name = input("Enter task name (max 30 characters): ")
        if len(name) > 30:
            print("Name too long. Please enter a name with maximum 30 characters.\n")
            continue
        break

    while True:
        description = input("Enter task description (max 50 characters): ")
        if len(description) > 50:
            print("Description too long. Please enter a description with maximum 50 characters.\n")
            continue
        break

    while True:
        due_date = input("Enter task due date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.\n")
            continue
        break

    status = "In Progress"
    tasks.append({'name': name, 'description': description, 'due_date': due_date, 'status': status})
    print("Task added successfully!")

# Define a function to delete a task
def delete_task():
    if not tasks:
        print("No tasks added yet!\n")
        return

    display_tasks()
    task_num = int(input("Enter the task number you want to delete: "))
    del tasks[task_num-1]
    print("Task deleted successfully!")

# Define a function to update a task
def update_task():
    if not tasks:
        print("No tasks added yet!\n")
        return

    display_tasks()
    task_num = int(input("Enter the task number you want to update: "))
    task = tasks[task_num-1]

    while True:
        name = input(f"Enter new name for '{task['name']}' (max 30 characters) (type 'same' to keep the same name): ")
        if name.lower() == "same":
            name = task['name']
            break
        if len(name) > 30:
            print("Name too long. Please enter a name with maximum 30 characters.\n")
            continue
        break

    while True:
        description = input(f"Enter new description for '{task['description']}' (max 50 characters) (type 'same' to keep the same description): ")
        if description.lower() == "same":
            description = task['description']
            break
        if len(description) > 50:
            print("Description too long. Please enter a description with maximum 50 characters.\n")
            continue
        break

    while True:
        due_date = input(f"Enter new due date for '{task['due_date']}' (YYYY-MM-DD) (type 'same' to keep the same due date): ")
        if due_date.lower() == "same":
            due_date = task['due_date']
            break
        try:
            datetime.datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.\n")
            continue
        break

    while True:
        status = input(f"Enter new status for '{task['status']}' (e.g. In Progress, Completed) (type 'same' to keep the same status): ")
        if status.lower() == "same":
            status = task['status']
            break
        if status not in ["In Progress", "Completed"]:
            print("Invalid status. Please enter a status of 'In Progress' or 'Completed'.\n")
            continue
        break

    tasks[task_num-1] = {'name': name, 'description': description, 'due_date': due_date, 'status': status}
    print("Task updated successfully!")

# Define a main function to run the Todo List app
def main():
    # Main loop of the program
    while True:
        print("Please select an option:")
        print("1. Display tasks")
        print("2. Add a new task")
        print("3. Delete a task")
        print("4. Update a task")
        print("5. Exit")
        choice = input()

        if choice == "1":
            display_tasks()

        elif choice == "2":
            add_task()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            update_task()

        elif choice == "5":
            break

        else:
            print("Invalid input. Please try again.\n")

if __name__ == "__main__":
    main()


