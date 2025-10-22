from task_manager import TaskManager
from ai_service import suggest_task_decomposition

def print_welcome_message():
    print("\n Welcome to the Task Manager!")
    
def print_menu():
    print("\n--- Intelligent Task Manager ---")
    print("1. Add Task")
    print("2. Add Task with AI Assistance")
    print("3. List Tasks")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

def main():

    task_manager = TaskManager()
    
    while True:
        print_welcome_message()
        print_menu()

        choice = input("Choose an option: ")

        match choice:
            case "1":
                description = input("Enter task description: ")
                priority = input("Enter task priority (Low, Medium, High): ")
                task_manager.add_task(description, priority)
            case "2":
                description = input("Enter task description: ")
                subtasks = suggest_task_decomposition(description)
                for subtask in subtasks:
                    if not subtask.startswith("Error:"):
                        task_manager.add_task(subtask, "Medium")
                    else:
                        print(subtask)
                        break
            case "3":
                task_manager.list_tasks()
            case "4":
                id_input = input("Enter task ID to complete: ")
                try:
                    task_id = int(id_input)
                    task_manager.complete_task(task_id)
                except ValueError:
                    print("Invalid task ID. Please enter a number.")

            case "5":
                id_input = input("Enter task ID to delete: ")
                try:
                    task_id = int(id_input)
                    task_manager.delete_task(task_id)
                except ValueError:
                    print("Invalid task ID. Please enter a number.")

            case "6":
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()