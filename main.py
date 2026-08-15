tasks = []


def add_task(name, description):
    name = name.strip().capitalize()
    description = description.strip().capitalize()
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
    status = status.strip().capitalize()
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
    name = name.strip().capitalize()
    description = description.strip().capitalize()

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
        print("This request is already completed.")
        return

    found_task["status"] = "Completed"


def mark_task_pending(identifier):
    found_task = find_task_by_id(identifier)

    if not found_task:
        print("The identifier does not exist.")
        return

    if found_task["status"] != "Completed":
        print("This request is already pending.")
        return

    found_task["status"] = "Pending"


def find_task_by_id(identifier):
    for task in tasks:
        if identifier == task["id"]:
            return task

    return None
