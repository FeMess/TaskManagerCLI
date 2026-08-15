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
        identifier = max(identifier, task["ID"])

    identifier = identifier + 1
    tasks.append(
        {
            "ID": identifier,
            "name": name,
            "description": description,
            "status": status,
        }
    )


def list_tasks(status):
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
            f"{task['ID']} | {task['name']} | {task['status']} | {task['description']} "
        )
