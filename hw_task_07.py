"""
Задание №7
Создать RESTful API для управления списком задач. Приложение должно
использовать FastAPI и поддерживать следующие функции:
- Получение списка всех задач.
- Получение информации о задаче по её ID.
- Добавление новой задачи.
- Обновление информации о задаче по её ID.
- Удаление задачи по её ID.
- Каждая задача должна содержать следующие поля: ID (целое число),
Название (строка), Описание (строка), Статус (строка): "todo", "in progress", "done"
- Создайте модуль приложения и настройте сервер и маршрутизацию.
- Создайте класс Task с полями id, title, description и status.
- Создайте список tasks для хранения задач.
- Создайте функцию get_tasks для получения списка всех задач (метод GET).
- Создайте функцию get_task для получения информации о задаче по её ID (метод GET).
- Создайте функцию create_task для добавления новой задачи (метод POST).
- Создайте функцию update_task для обновления информации о задаче по её ID (метод PUT).
- Создайте функцию delete_task для удаления задачи по её ID (метод DELETE)
"""

from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from random import choice

app = FastAPI()
templates = Jinja2Templates(directory='./lesson_5/seminar_5/templates')


class Task(BaseModel):
    id: int
    task_title: str
    description: str
    status: str


tasks = []
statuses = ['todo', 'in progress', 'done']
for i in range(1, 11):
    new_task = Task(id=i, task_title=f'title_task_{i}',
                    description=f'description_task_{i}',
                    status=choice(statuses))
    tasks.append(new_task)


@app.get('/tasks/', response_class=HTMLResponse)
async def get_tasks(request: Request):
    return templates.TemplateResponse('tasks.html', {'request': request, 'tasks': tasks, 'title': 'Список задач'})


@app.get('/tasks/{task_id}', response_model=Task)
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail='Task not found')


@app.post('/tasks/', response_model=Task)
async def create_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, edit_task: Task):
    for num, task in enumerate(tasks):
        if task.id == task_id:
            task.id = task_id
            tasks[num] = edit_task
            return edit_task
    raise HTTPException(status_code=404, detail=f'Task not found')


@app.delete('/tasks/{task_id}', response_model=Task)
async def delete_task(task_id: int):
    for num, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(num)
