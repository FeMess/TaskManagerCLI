import os
from time import sleep


class CLI:
    def __init__(self, manager):
        self.manager = manager

    def present_system(self):
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
                sleep(2)
                continue

            elif user_choice == "0":
                return

            elif user_choice == "1":
                self.show_header()

                task_name = input("Task Name: ")
                task_description = input("Task Description: ")

                manager_response = self.manager.add_task(task_name, task_description)

                if manager_response == False:
                    print("The task must have a name.")
                    sleep(2)
                elif manager_response == True:
                    print("The task has been created successfully.")
                    sleep(2)

            elif user_choice == "2":
                self.show_header()

                task_status = input("Status [Pending, Completed, All]: ")

                manager_response = self.manager.list_tasks(task_status)

                if manager_response == False:
                    print(
                        "Invalid value for status. Try to use [Pending, Completed, All]"
                    )
                    sleep(2)

                elif manager_response is None:
                    print("There are no tasks available for this status.")
                    sleep(2)

                elif manager_response:
                    for task in manager_response:
                        print(
                            f"{task.id} | {task.name} | {task.status} | {task.description}"
                        )
                    sleep(2)

            elif user_choice == "3":
                self.show_header()

                filtered_tasks = self.manager.list_tasks()

                for task in filtered_tasks:
                    print(
                        f"{task.id} | {task.name} | {task.status} | {task.description}"
                    )

                task_ID = int(input("\nWhich task would you like to update? "))
                task_name = input("New task name? ")
                task_description = input("New task description? ")

                manager_response = self.manager.update_task(
                    task_name, task_description, task_ID
                )

                if manager_response == False:
                    print("The task must have a name.")
                    sleep(2)

                elif manager_response is None:
                    print("The defined identifier does not exist.")
                    sleep(2)

                elif manager_response == True:
                    print("The task has been updated successfully.")
                    sleep(2)

    def show_header(self):
        os.system("cls")

        print("Task Manager\n")

    def validate_id_input(self, identifier):
        pass
