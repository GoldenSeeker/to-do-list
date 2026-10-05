import json  # this allows the program to save tasks in a JSON format, which is more structured and easier to read than plain text

tasks = []

try:  # this allows the program to run without crashing even if it fails
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    pass  # If the file doesn't exist, it starts with an empty task list


def save_tasks():  # this function saves the tasks to a file
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1): #loops with a counter starting at 1
        status = "[Done]" if task.get("done") else "[Not Done]" #picks a check or empty box based on the done value
        print(f"{i}. {task['task']} {status}")

print("Welcome to the To-Do List App")
while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the new task: ")
        tasks.append({"task": task, "done": False})
        save_tasks()
        print(f'Task "{task}" added.')
    elif choice == "2":
        show_tasks()
        
    elif choice == "3":
        if not tasks:
            print("No tasks to mark as done.")
        else:
            show_tasks()
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} {('[Done]' if task.get('done') else '[Not Done]')}")
            try:
                task_num = int(input("Enter the number of the task to mark as done: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["done"] = True
                    save_tasks()
                    print(f'Task "{tasks[task_num - 1]["task"]}" marked as done.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "4":
        if not tasks:
            print("No tasks to remove.")
        else:
            show_tasks()
            try:
                task_num = int(input("Enter the number of the task to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    save_tasks()
                    print(f'Task "{removed_task["task"]}" removed.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        #Ngl made a shit tonne of mistakes in this code, but I think it works now. I will try to make it better in the future.