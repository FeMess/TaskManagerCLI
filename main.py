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
