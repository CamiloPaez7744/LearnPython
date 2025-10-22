class Task:
    def __init__(self, id, description, priority, completed=False):
        self.id = id
        self.description = description
        self.priority = priority
        self.completed = completed

    def __str__(self):
        status = "" if self.completed else " "
        return f"[{status}] (ID: {self.id}) {self.description} - Priority: {self.priority}"

class TaskManager:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description, priority):
        task = Task(self._next_id, description, priority)
        self._tasks.append(task)
        self._next_id += 1
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
                return task
        print("Task not found.")
        return None

    def get_pending_tasks(self):
        return [task for task in self._tasks if not task.completed]

    def get_all_tasks(self):
        return self._tasks

    def delete_task(self, task_id):
        self._tasks = [task for task in self._tasks if task.id != task_id]