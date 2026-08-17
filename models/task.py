class Task:
    def __init__(self, identifier: int, name: str, description: str):
        self.id = identifier
        self.name = name
        self.description = description
        self.status = "Pending"
