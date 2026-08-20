from models.cli import CLI
from models.task_manager import TaskManager

if __name__ == "__main__":
    manager = TaskManager()
    cli_interface = CLI(manager)

    cli_interface.present_system()
