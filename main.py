import json  # This is a structured storage making it easy to read/edit

TASKS_FILE = "tasks.json"

#Load
try:
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []          # First run: start empty
except json.JSONDecodeError:
    print("Warning: tasks.json was corrupt. Starting with an empty list.")
    tasks = []


#Helpers
def save_tasks() -> None:
    """Persist the current task list to disk."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(only_unfinished: bool = False) -> None:
    """Print tasks, optionally filtering out finished ones."""
    print("Tasks:")
    found = False
    for i, task in enumerate(tasks, start=1):
        if only_unfinished and task.get("done"):
            continue
        status = "[Done]" if task["done"] else "[Not Done]"
        print(f"{i}. {task['task']} {status}")
        found = True
    if not found:
        print("No tasks found.")


def get_task_number(message: str):
    """Prompt until a valid task index (0-based) is entered, or return None."""
    try:
        num = int(input(message))
    except ValueError:
        print("Please enter a valid number.")
        return None
    if 1 <= num <= len(tasks):
        return num - 1
    print("Invalid task number.")
    return None


def prompt_nonempty(prompt: str) -> str:
    """Keep asking until the user types something non-blank."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Task cannot be empty.")


#Main loop
def main() -> None:
    print("Welcome to the To-Do List App")
    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. View unfinished tasks")
        print("4. Mark a task as done")
        print("5. Remove a task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            task = prompt_nonempty("Enter the new task: ")
            tasks.append({"task": task, "done": False})
            save_tasks()
            print(f'Task "{task}" added.')

        elif choice == "2":
            if not tasks:
                print("No tasks to show.")
            else:
                show_tasks()

        elif choice == "3":
            unfinished = [t for t in tasks if not t.get("done")]
            if not unfinished:
                print("No unfinished tasks to show.")
            else:
                show_tasks(only_unfinished=True)

        elif choice == "4":
            if not tasks:
                print("No tasks to mark as done.")
                continue
            show_tasks()
            idx = get_task_number("Enter the number of the task to mark as done: ")
            if idx is not None:
                tasks[idx]["done"] = True
                save_tasks()
                print(f'Task "{tasks[idx]["task"]}" marked as done.')

        elif choice == "5":
            if not tasks:
                print("No tasks to remove.")
                continue
            show_tasks()
            idx = get_task_number("Enter the number of the task to remove: ")
            if idx is not None:
                removed = tasks.pop(idx)
                save_tasks()
                print(f'Task "{removed["task"]}" removed.')

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main() #Not useful yet but will be in the future when more features are added.