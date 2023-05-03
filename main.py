TODO_FILE = "todo.txt"


def print_todo_list(todo_list):
    """Prints the current to-do list"""
    if not todo_list:
        print("No tasks found.")
    else:
        print("Current tasks:")
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. {task}")


def add_task(todo_list):
    """Adds a new task to the to-do list"""
    task = input("Enter a new task: ")
    todo_list.append(task)
    save_todo_list(todo_list)
    print(f"Task \"{task}\" added.")


def remove_task(todo_list):
    """Removes a task from the to-do list"""
    task_number = int(input("Enter the number of the task to remove: "))
    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number.")
    else:
        task = todo_list.pop(task_number - 1)
        save_todo_list(todo_list)
        print(f"Task \"{task}\" removed.")


def edit_task(todo_list):
    """Edits an existing task on the to-do list"""
    task_number = int(input("Enter the number of the task to edit: "))
    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number.")
    else:
        new_task = input("Enter the new task: ")
        old_task = todo_list[task_number - 1]
        todo_list[task_number - 1] = new_task
        save_todo_list(todo_list)
        print(f"Task \"{old_task}\" changed to \"{new_task}\".")


def save_todo_list(todo_list):
    """Saves the to-do list to a file"""
    with open(TODO_FILE, "w") as f:
        for task in todo_list:
            f.write(f"{task}\n")


def load_todo_list():
    """Loads the to-do list from a file"""
    todo_list = []
    try:
        with open(TODO_FILE, "r") as f:
            for line in f:
                todo_list.append(line.strip())
    except FileNotFoundError:
        pass
    return todo_list


def main():
    todo_list = load_todo_list()

    while True:
        print_todo_list(todo_list)
        print("\nMenu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Edit task")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice.")
            continue

        if choice == 1:
            add_task(todo_list)
        elif choice == 2:
            remove_task(todo_list)
        elif choice == 3:
            edit_task(todo_list)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
