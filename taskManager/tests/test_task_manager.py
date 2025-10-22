import json
from pathlib import Path

import pytest

from task_manager import TaskManager, Task


def test_add_and_get_tasks(tmp_path):
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    mgr = TaskManager()

    # Initially empty
    assert mgr.get_all_tasks() == []
    assert mgr.get_pending_tasks() == []

    # Act: add tasks
    t1 = mgr.add_task("Write tests", 2)
    t2 = mgr.add_task("Fix bug", 1)

    # Assert: task objects and ids
    assert isinstance(t1, Task)
    assert isinstance(t2, Task)
    assert t1.id == 1
    assert t2.id == 2
    assert t1.description == "Write tests"
    assert t2.priority == 1
    assert t1.completed is False

    # Assert: getters
    all_tasks = mgr.get_all_tasks()
    pending = mgr.get_pending_tasks()
    assert len(all_tasks) == 2
    assert len(pending) == 2

    # Assert: string representation includes expected pieces
    s = str(t1)
    assert "Write tests" in s
    assert "Priority: 2" in s
    assert "ID: 1" in s
    assert "✓" not in s  # not completed yet


def test_complete_task_and_persistence(tmp_path):
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    mgr = TaskManager()
    t = mgr.add_task("Do laundry", 3)

    # Complete the task
    returned = mgr.complete_task(t.id)
    assert returned is not None
    assert returned.completed is True

    # Pending should be empty now
    assert mgr.get_pending_tasks() == []

    # Reload manager to ensure persistence
    mgr2 = TaskManager()
    tasks = mgr2.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == t.id
    assert tasks[0].completed is True
    assert tasks[0].description == "Do laundry"


def test_delete_task_and_persistence(tmp_path):
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    mgr = TaskManager()
    a = mgr.add_task("First", 1)
    b = mgr.add_task("Second", 2)

    # Delete first task
    mgr.delete_task(a.id)
    remaining = mgr.get_all_tasks()
    assert len(remaining) == 1
    assert remaining[0].id == b.id
    assert remaining[0].description == "Second"

    # Reload and ensure deletion persisted
    mgr2 = TaskManager()
    remaining2 = mgr2.get_all_tasks()
    assert len(remaining2) == 1
    assert remaining2[0].id == b.id


def test_id_increment_after_reload(tmp_path):
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    mgr = TaskManager()
    t1 = mgr.add_task("Initial", 5)
    assert t1.id == 1

    # Create a new manager that reads from the same file
    mgr2 = TaskManager()
    t2 = mgr2.add_task("Next", 4)
    # id should continue from existing max id
    assert t2.id == 2


def test_load_handles_missing_and_corrupt_json(tmp_path):
    # Missing file scenario
    missing_file = tmp_path / "missing.json"
    TaskManager.FILENAME = str(missing_file)
    # Ensure file doesn't exist
    if missing_file.exists():
        missing_file.unlink()
    mgr_missing = TaskManager()
    assert mgr_missing.get_all_tasks() == []
    # Next id should start at 1
    t = mgr_missing.add_task("New after missing", 1)
    assert t.id == 1

    # Corrupt JSON scenario
    corrupt_file = tmp_path / "corrupt.json"
    corrupt_file.write_text("{ not: valid json }")
    TaskManager.FILENAME = str(corrupt_file)
    mgr_corrupt = TaskManager()
    # Should recover to empty task list
    assert mgr_corrupt.get_all_tasks() == []
    # Adding a task should start from 1
    t2 = mgr_corrupt.add_task("Recover", 2)
    assert t2.id == 1


def test_save_file_format(tmp_path):
    TaskManager.FILENAME = str(tmp_path / "out.json")
    mgr = TaskManager()
    t = mgr.add_task("Format check", 7)

    # Read the file directly and assert JSON structure
    path = Path(TaskManager.FILENAME)
    assert path.exists()
    raw = path.read_text()
    data = json.loads(raw)
    assert isinstance(data, list)
    assert len(data) == 1
    entry = data[0]
    # Keys and types
    assert set(entry.keys()) >= {"id", "description", "priority", "completed"}
    assert entry["id"] == t.id
    assert entry["description"] == "Format check"
    assert entry["priority"] == 7
    assert entry["completed"] is False
