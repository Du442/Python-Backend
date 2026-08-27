from pydantic import BaseModel
from fastapi import FastAPI

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

app = FastAPI()

tasks: list[Task] = []

@app.get('/tasks')
def get_tasks():
    return {"id":id, "title":title, "done":done}

@app.post('/tasks', response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return tasks

@app.get('/tasks/{task_id}')
def get_specific_task(task_id: int):
    return {"message": f'task id {task_id} created'}

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    return {"message": f'task id {task_id} deleted'}