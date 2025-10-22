from task_manager import TaskManager

def print_welcome_message():
    print("\n Welcome to the Task Manager!")
    
def print_menu():
    print("\n--- Intelligent Task Manager ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

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
                task_manager.list_tasks()
                
            case "3":
                id_input = input("Enter task ID to complete: ")
                try:
                    task_id = int(id_input)
                    task_manager.complete_task(task_id)
                except ValueError:
                    print("Invalid task ID. Please enter a number.")

            case "4":
                id_input = input("Enter task ID to delete: ")
                try:
                    task_id = int(id_input)
                    task_manager.delete_task(task_id)
                except ValueError:
                    print("Invalid task ID. Please enter a number.")

            case "5":
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()