import json
class Task:
    def __init__(self, id, description, priority, completed=False):
        self.id = id
        self.description = description
        self.priority = priority
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] (ID: {self.id}) {self.description} - Priority: {self.priority}"

class TaskManager:
    
    FILENAME = "tasks.json"
    
    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description, priority):
        task = Task(self._next_id, description, priority)
        self._tasks.append(task)
        self._next_id += 1
        self.save_tasks()
        return task
    
    def list_tasks(self):
        if not self._tasks:
            print("No tasks available.")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                print(f"Task completed: {task}")
                self.save_tasks()
                return task
        print("Task not found.")
        return None

    def get_pending_tasks(self):
        return [task for task in self._tasks if not task.completed]

    def get_all_tasks(self):
        return self._tasks

    def delete_task(self, task_id):
        self._tasks = [task for task in self._tasks if task.id != task_id]
        self.save_tasks()
        
    def save_tasks(self):
        with open(self.FILENAME, 'w') as f:
            json.dump([task.__dict__ for task in self._tasks], f)

    def load_tasks(self):
        try:
            with open(self.FILENAME, 'r') as f:
                tasks_data = json.load(f)
                self._tasks = [Task(**task) for task in tasks_data]
                self._next_id = max(task.id for task in self._tasks) + 1 if self._tasks else 1
        except FileNotFoundError:
            self._tasks = []
            self._next_id = 1
        except json.JSONDecodeError:
            self._tasks = []
            self._next_id = 1