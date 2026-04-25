from fastapi import FastAPI
from services.task_service import get_tasks, create_task, delete_task, complete_task

app = FastAPI()


@app.get("/tasks")
def read_tasks():
    return get_tasks()


@app.post("/tasks")
def add_task(title: str, description: str, date: str):
    create_task(title, description, date)
    return {"message": "Task created"}


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    delete_task(task_id)
    return {"message": "Task deleted"}


@app.put("/tasks/{task_id}/complete")
def complete(task_id: int):
    complete_task(task_id)
    return {"message": "Task completed"}