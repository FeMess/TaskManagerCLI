import os
from time import sleep

tasks = []


def add_task(name, description):
    name = name.strip().title()
    description = description.strip().title()
    status = "Pending"
    identifier = 0

    if name == "":
        print("The task must have a name.")
        return

    for task in tasks:
        identifier = max(identifier, task["id"])

    identifier = identifier + 1

    tasks.append(
        {
            "id": identifier,
            "name": name,
            "description": description,
            "status": status,
        }
    )


def list_tasks(status="All"):
    status = status.strip().title()
    filtered_tasks = []

    if status not in ["Pending", "Completed", "All"]:
        print("Invalid value for status. Try to use [Pending, Completed, All]")
        return

    for task in tasks:
        if task["status"] == status or status == "All":
            filtered_tasks.append(task)

    if not filtered_tasks:
        print("There are no tasks available for this status.")
        return

    for task in filtered_tasks:
        print(
            f"{task['id']} | {task['name']} | {task['status']} | {task['description']}"
        )


def update_task(identifier, name, description):
    name = name.strip().title()
    description = description.strip().title()

    if name == "":
        print("The task must have a name.")
        return

    found_task = find_task_by_id(identifier)

    if not found_task:
        print("The identifier does not exist.")
        return

    found_task["name"] = name
    found_task["description"] = description


def remove_task(identifier):
    found_task = find_task_by_id(identifier)

    if not found_task:
        print("The identifier does not exist.")
        return

    tasks.remove(found_task)


def view_task(identifier):
    found_task = find_task_by_id(identifier)

    if not found_task:
        print("The identifier does not exist.")
        return

    print(
        f"{found_task['id']} | {found_task['name']} | {found_task['status']} | {found_task['description']}"
    )


def mark_task_completed(identifier):
    found_task = find_task_by_id(identifier)

    if not found_task:
        print("The identifier does not exist.")
        return

    if found_task["status"] != "Pending":
        print("This task is already completed.")
        return

    found_task["status"] = "Completed"


def mark_task_pending(identifier):
    found_task = find_task_by_id(identifier)

    if not found_task:
        print("The identifier does not exist.")
        return

    if found_task["status"] != "Completed":
        print("This task is already pending.")
        return

    found_task["status"] = "Pending"


def find_task_by_id(identifier):
    identifier = validate_id(identifier)

    if identifier is not None:
        for task in tasks:
            if identifier == task["id"]:
                return task
    return None


def validate_id(identifier):
    try:
        identifier = int(identifier)
        return identifier
    except ValueError:
        print("The identifier does not exist.")
        return None


def show_header():
    os.system("cls")
    print("Task Manager\n")


def present_system():
    while True:
        os.system("cls")

        print("Task Manager, Welcome.\n")
        print("[0] - Exit")
        print("[1] - New Task")
        print("[2] - List Tasks")
        print("[3] - Update Task")
        print("[4] - Remove Task")
        print("[5] - View Specific Task")
        print("[6] - Mark as Completed")
        print("[7] - Mark as Pending\n")

        user_choice = input("What do you want to do? ").strip()

        if user_choice not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid option. Please, select a valid value.")
            sleep(3)
            continue

        if user_choice == "0":
            return

        elif user_choice == "1":
            show_header()

            task_name = input("Task name: ")
            task_description = input("Task description: ")

            add_task(task_name, task_description)

        elif user_choice == "2":
            show_header()

            task_status = input("Status [Pending, Completed, All]: ")

            list_tasks(task_status)
            input("\nPress enter to continue: ")

        elif user_choice == "3":
            show_header()

            list_tasks()
            task_id = input("\nWhich task do you want to update? ")
            task_name = input("New task name: ")
            task_description = input("New task description: ")

            update_task(task_id, task_name, task_description)

        elif user_choice == "4":
            show_header()

            list_tasks()
            task_id = input("\nWhich task do you want to remove? ")

            remove_task(task_id)

        elif user_choice == "5":
            show_header()

            list_tasks()
            task_id = input("\nWhich task do you want to see the details? ")

            view_task(task_id)
            input("\nPress enter to continue: ")

        elif user_choice == "6":
            show_header()

            list_tasks("Pending")
            task_id = input("\nWhich task do you want to mark as completed? ")

            mark_task_completed(task_id)

        elif user_choice == "7":
            show_header()

            list_tasks("Completed")
            task_id = input("\nWhich task do you want to mark as pending? ")

            mark_task_pending(task_id)
