"""
Задание №2
Создать веб-приложение на FastAPI, которое будет предоставлять API для
работы с базой данных пользователей. Пользователь должен иметь
следующие поля:
- ID (автоматически генерируется при создании пользователя)
- Имя (строка, не менее 2 символов)
- Фамилия (строка, не менее 2 символов)
- Дата рождения (строка в формате "YYYY-MM-DD")
- Email (строка, валидный email)
- Адрес (строка, не менее 5 символов)
API должен поддерживать следующие операции:
- Добавление пользователя в базу данных
- Получение списка всех пользователей в базе данных
- Получение пользователя по ID
- Обновление пользователя по ID
- Удаление пользователя по ID
Приложение должно использовать базу данных SQLite3 для хранения
пользователей.
"""

import sqlalchemy
import databases
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from datetime import date

DATABASE_URL = 'sqlite:///lesson_6/seminar_6/hw_task_02/users_database.db'
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('first_name', sqlalchemy.String(50)),
    sqlalchemy.Column('last_name', sqlalchemy.String(50)),
    sqlalchemy.Column('date_of_birth', sqlalchemy.String(10)),
    sqlalchemy.Column('email', sqlalchemy.String(50)),
    sqlalchemy.Column('address', sqlalchemy.String(128))
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={'check_same_thread': False}
)
metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    first_name: str = Field(..., title='First Name', min_length=4, max_length=50)
    last_name: str = Field(..., title='Last Name', min_length=4, max_length=50)
    date_of_birth: str = Field(..., title='Date of Birth')
    email: str = Field(..., title='Email', min_length=10, max_length=50)
    address: str = Field(title='Password', max_length=128)


class User(BaseModel):
    id: int
    first_name: str = Field(..., title='First Name', min_length=4, max_length=50)
    last_name: str = Field(..., title='Last Name', min_length=4, max_length=50)
    date_of_birth: str = Field(..., title='Date of Birth')
    email: str = Field(..., title='Email', min_length=10, max_length=50)
    address: str = Field(title='Password', max_length=128)


# @app.get('/fake_users/{count}')
# async def create_note(count: int):
#     for i in range(1, count):
#         query = users.insert().values(first_name=f'first_name_{i}', last_name=f'last_name_{i}',
#                                       date_of_birth=f'{date.today()}', email=f'mail_{i}@mail.ru',
#                                       address=f'address_{i}')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


@app.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post('/users/', response_model=User)
async def create_user(new_user: UserIn):
    query = users.insert().values(**new_user.dict())
    last_record_id = await database.execute(query)
    return {**new_user.dict(), 'id': last_record_id}


@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, upd_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**upd_user.dict())
    await database.execute(query)
    return {**upd_user.dict(), 'id': user_id}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f'User ID {user_id} deleted'}
