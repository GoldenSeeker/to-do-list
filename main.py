tasks = []

try: #this allows the program to run without crashing even if it fails
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass  # If the file doesn't exist, it starts with an empty task list

def save_tasks(): # this function saves the tasks to a file
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

print("Welcome to the To-Do List App")
while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the new task: ")
        tasks.append(task)
        save_tasks()
        print(f'Task "{task}" added.')
    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the number of the task to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f'Task "{removed_task}" removed.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")