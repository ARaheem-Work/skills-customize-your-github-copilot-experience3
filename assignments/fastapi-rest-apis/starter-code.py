"""Starter code for the FastAPI REST APIs assignment."""

from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: List[Task] = []


@app.get("/tasks")
def list_tasks():
    # Task 1: Return all tasks.
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task_input: TaskCreate):
    # Task 1: Add a new task using the next available ID.
    next_id = len(tasks) + 1
    task = Task(id=next_id, **task_input.model_dump())
    tasks.append(task)
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Task 2: Find and return a single task by ID.
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_input: TaskCreate):
    # Task 2: Update an existing task by ID.
    for i, task in enumerate(tasks):
        if task.id == task_id:
            updated = Task(id=task_id, **task_input.model_dump())
            tasks[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    # Task 2: Delete a task by ID.
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
