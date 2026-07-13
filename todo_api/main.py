from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Store tasks in a Python list
todos = []

# Model for creating a task
class TodoCreate(BaseModel):
    title: str

# Model for updating a task
class TodoUpdate(BaseModel):
    title: str
    completed: bool


# Question 1: Add a new task
@app.post("/todos")
def add_todo(todo: TodoCreate):
    new_task = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": False
    }
    todos.append(new_task)
    return new_task


# Question 2: Get all tasks
@app.get("/todos")
def get_todos():
    return todos


# Question 3: Get task by ID
@app.get("/todos/{id}")
def get_todo(id: int):
    for todo in todos:
        if todo["id"] == id:
            return todo
    raise HTTPException(status_code=404, detail="Task not found")


# Question 4: Update task
@app.put("/todos/{id}")
def update_todo(id: int, updated_todo: TodoUpdate):
    for todo in todos:
        if todo["id"] == id:
            todo["title"] = updated_todo.title
            todo["completed"] = updated_todo.completed
            return todo
    raise HTTPException(status_code=404, detail="Task not found")


# Question 5: Delete task
@app.delete("/todos/{id}")
def delete_todo(id: int):
    for todo in todos:
        if todo["id"] == id:
            todos.remove(todo)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

