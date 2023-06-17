"""
Задание №6
Необходимо создать базу данных для интернет-магазина.
База данных должна состоять из трех таблиц: товары, заказы и пользователи.
Таблица товары должна содержать информацию о доступных товарах, их описаниях и ценах.
Таблица пользователи должна содержать информацию о зарегистрированных пользователях магазина.
Таблица заказы должна содержать информацию о заказах, сделанных пользователями.
- Таблица пользователей должна содержать следующие поля:
id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
- Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
название, описание и цена.
- Таблица заказов должна содержать следующие поля:
id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа
- Создайте модели pydantic для получения новых данных
и возврата существующих в БД для каждой из трёх таблиц (итого шесть моделей).
- Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API (итого 15 маршрутов):
- Чтение всех
- Чтение одного
- Запись
- Изменение
- Удаление
"""

import sqlalchemy
import databases
from pydantic import BaseModel, Field

DATABASE_URL = 'sqlite:///lesson_6/seminar_6/hw_task_06/store_database.db'
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('first_name', sqlalchemy.String(50)),
    sqlalchemy.Column('last_name', sqlalchemy.String(50)),
    sqlalchemy.Column('email', sqlalchemy.String(50)),
    sqlalchemy.Column('password', sqlalchemy.String(128))
)

products = sqlalchemy.Table(
    'products',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('title', sqlalchemy.String(64)),
    sqlalchemy.Column('description', sqlalchemy.String(128)),
    sqlalchemy.Column('price', sqlalchemy.Integer)
)

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('product_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id')),
    sqlalchemy.Column('order_date', sqlalchemy.String(10)),
    sqlalchemy.Column('order_status', sqlalchemy.String(50))
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={'check_same_thread': False}
)

metadata.create_all(engine)
statuses = ['received', 'in processing', 'packed', 'paid for', 'not paid', 'shipped', 'delivered']


class UserIn(BaseModel):
    first_name: str = Field(..., title='First Name', min_length=4, max_length=50)
    last_name: str = Field(..., title='Last Name', min_length=4, max_length=50)
    email: str = Field(..., title='Email', min_length=10, max_length=50)
    password: str = Field(..., title='Password', max_length=128)


class User(BaseModel):
    id: int
    first_name: str = Field(..., title='First Name', min_length=4, max_length=50)
    last_name: str = Field(..., title='Last Name', min_length=4, max_length=50)
    email: str = Field(..., title='Email', min_length=10, max_length=50)
    password: str = Field(..., title='Password', max_length=128)


class ProductIn(BaseModel):
    title: str = Field(..., title='Title', min_length=4, max_length=50)
    description: str = Field(..., title='Description', min_length=4, max_length=128)
    price: int = Field(..., title='Price')


class Product(BaseModel):
    id: int
    title: str = Field(..., title='Title', min_length=4, max_length=50)
    description: str = Field(..., title='Description', min_length=4, max_length=128)
    price: int = Field(..., title='Price')


class OrderIn(BaseModel):
    user_id: int = Field(..., title='User ID')
    product_id: int = Field(..., title='Product ID')
    order_date: str = Field(..., title='Order Date')
    order_status: str = Field(..., title='Order Status')


class Order(BaseModel):
    id: int
    user_id: int = Field(..., title='User ID')
    product_id: int = Field(..., title='Product ID')
    order_date: str = Field(..., title='Order Date')
    order_status: str = Field(..., title='Order Status')
