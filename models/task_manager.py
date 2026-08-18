from models.task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

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

        return True

    def remove_task(self, identifier):
        found_task = self.find_task_by_id(identifier)

        if not found_task:
            return None

        self.tasks.remove(found_task)
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

        return True

    def mark_task_pending(self, identifier):
        found_task = self.find_task_by_id(identifier)

        if not found_task:
            return None

        if found_task.status != "Completed":
            return False

        found_task.status = "Pending"

        return True

    def find_task_by_id(self, identifier):
        for task in self.tasks:
            if task.id == identifier:
                return task
        return None
