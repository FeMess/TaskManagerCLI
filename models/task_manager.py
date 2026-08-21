import json

from models.task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, name, description):
        name = name.strip().title()
        description = description.strip().title()
        identifier = 0

        if name == "":
            return False

        for task in self.tasks:
            identifier = max(identifier, task.id)

        identifier = identifier + 1

        new_task = Task(identifier, name, description)
        self.tasks.append(new_task)
        self.save_tasks()

        return True

    def list_tasks(self, status="All"):
        status = status.strip().title()
        filtered_tasks = []

        if status not in ["Pending", "Completed", "All"]:
            return False

        for task in self.tasks:
            if task.status == status or status == "All":
                filtered_tasks.append(task)

        return filtered_tasks

    def update_task(self, name, description, identifier):
        name = name.strip().title()
        description = description.strip().title()

        if name == "":
            return False

        found_task = self.find_task_by_id(identifier)

        if not found_task:
            return None

        found_task.name = name
        found_task.description = description
        self.save_tasks()

        return True

    def remove_task(self, identifier):
        found_task = self.find_task_by_id(identifier)

        if not found_task:
            return None

        self.tasks.remove(found_task)
        self.save_tasks()

        return True

    def view_task(self, identifier):
        found_task = self.find_task_by_id(identifier)

        if not found_task:
            return None

        return found_task

    def mark_task_completed(self, identifier):
        found_task = self.find_task_by_id(identifier)

        if not found_task:
            return None

        if found_task.status != "Pending":
            return False

        found_task.status = "Completed"
        self.save_tasks()

        return True

    def mark_task_pending(self, identifier):
        found_task = self.find_task_by_id(identifier)

        if not found_task:
            return None

        if found_task.status != "Completed":
            return False

        found_task.status = "Pending"
        self.save_tasks()

        return True

    def find_task_by_id(self, identifier):
        for task in self.tasks:
            if task.id == identifier:
                return task
        return None

    def load_tasks(self):
        try:
            with open("data/tasks.json", "r") as file:
                json_tasks = json.load(file)
        except FileNotFoundError:
            with open("data/tasks.json", "w") as file:
                json.dump([], file)
                json_tasks = []
        except json.JSONDecodeError:
            json_tasks = []

        for task in json_tasks:
            new_task = Task(task["id"], task["name"], task["description"])
            new_task.status = task["status"]
            self.tasks.append(new_task)

    def save_tasks(self):
        list_tasks = []

        for task in self.tasks:
            list_tasks.append(
                {
                    "id": task.id,
                    "name": task.name,
                    "description": task.description,
                    "status": task.status,
                }
            )

        with open("data/tasks.json", "w") as file:
            json.dump(list_tasks, file, indent=4)
