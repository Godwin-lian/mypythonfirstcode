def display_menu():
    print("----- To-Do List Menu -----")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Remove Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def mark_task_completed(tasks):
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index.")
    else:
        tasks[task_index] += " (Completed)"
        print("Task marked as completed.")

def view_tasks(tasks):
    print("----- Tasks -----")
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

def remove_task(tasks):
    task_index = int(input("Enter the index of the task to remove: "))
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index.")
    else:
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' removed successfully.")

def todo_list():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_task_completed(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

todo_list()
