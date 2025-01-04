"""


1. CRUD Operations
- Creating API routes for `GET`, `POST`, `PUT`, and `DELETE` operations.
- Understanding how to handle data from requests using Pydantic models.

2. Error Handling
- Raising custom HTTP exceptions with `HTTPException`.
- How to handle cases like duplicate IDs or missing tasks.

3. Path and Query Parameters
- Using `@router.get("/{task_id}")` to accept dynamic path parameters.
- Querying or filtering data based on route parameters.

Usage in Code
- `@router.get` defines a GET endpoint to fetch tasks.
- `@router.post` defines a POST endpoint to create new tasks.
- `@router.put` and `@router.delete` allow updating and deleting tasks, respectively.


"""
from fastapi import APIRouter, HTTPException
from app.models import Task
from app.utils import load_tasks, save_tasks

router = APIRouter()
tasks = load_tasks()

@router.get("/tasks")
def get_tasks():
    return tasks

@router.post("/tasks")
def create_task(task: Task):
    if any(t['id'] == task.id for t in tasks):
        raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks.append(task.dict())
    save_tasks(tasks)
    return task

@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for idx, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks[idx] = updated_task.dict()
            save_tasks(tasks)
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return {"message": "Task deleted"}
