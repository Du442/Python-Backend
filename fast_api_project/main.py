from pydantic import BaseModel
from fastapi import FastAPI

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

app = FastAPI()

tasks = list()

@app.get('/tasks')
def get_tasks():
    return f'{tasks}'

@app.post('/tasks')
def create_task(task: Task):
    tasks.append(task)
    return tasks

@app.get('/tasks/{task_id}')
def get_specific_task(task_id: int):
    for i in tasks:
        if i.id == task_id:
            return f'{i.title} | {i.done}'
    return 'task not found'

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    for i in tasks:
        if i.id == task_id:
            tasks.remove(i)
            return tasks
    return 'task not found'