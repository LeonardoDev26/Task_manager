from fastapi import FastAPI
from services.task_service import get_tasks, create_task, delete_task, complete_task
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskCreate(BaseModel):
    title: str
    description: str
    date: str


@app.get("/tasks")
def read_tasks():
    return get_tasks()

from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    date: str

@app.post("/tasks")
def add_task(task: Task):
    create_task(task.title, task.description, task.date)
    return {"message": "Task created"}

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    delete_task(task_id)
    return {"message": "Task deleted"}

@app.put("/tasks/{task_id}/complete")
def complete(task_id: int):
    complete_task(task_id)
    return {"message": "Task completed"}