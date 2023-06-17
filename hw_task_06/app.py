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

import uvicorn
from lesson_6.seminar_6.hw_task_06.models import database, statuses,\
    users, products, orders, User, UserIn, Product, ProductIn, Order, OrderIn
from fastapi import FastAPI
from typing import List
from random import randint, choice
from datetime import date

app = FastAPI()


# @app.get('/fake_users/{count}')
# async def create_fake_users(count: int):
#     for i in range(1, count + 1):
#         query = users.insert().values(first_name=f'first_name_{i}', last_name=f'last_name_{i}',
#                                       email=f'mail_{i}@mail.ru', password=f'address_{i}')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}
#
#
# @app.get('/fake_products/{count}')
# async def create_fake_products(count: int):
#     for i in range(1, count + 1):
#         query = products.insert().values(title=f'title_product_{i}', description=f'description_product_{i}',
#                                          price=randint(200, 10000))
#         await database.execute(query)
#     return {'message': f'{count} fake product create'}
#
#
# @app.get('/fake_orders/{count}')
# async def create_fake_orders(count: int):
#     for i in range(1, count):
#         query = orders.insert().values(user_id=randint(1, 10), product_id=randint(1, 15),
#                                        order_date=date.today(), order_status=choice(statuses))
#         await database.execute(query)
#     return {'message': f'{count} fake product create'}


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


@app.get('/products/', response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.get('/products/{product_id}', response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@app.post('/products/', response_model=Product)
async def create_product(new_product: ProductIn):
    query = products.insert().values(**new_product.dict())
    last_record_id = await database.execute(query)
    return {**new_product.dict(), 'id': last_record_id}


@app.put('/products/{product_id}', response_model=Product)
async def update_product(product_id: int, upd_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**upd_product.dict())
    await database.execute(query)
    return {**upd_product.dict(), 'id': product_id}


@app.delete('/products/{product_id}')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': f'Product ID {product_id} deleted'}


@app.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get('/orders/{order_id}', response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.post('/orders/', response_model=Order)
async def create_order(new_order: OrderIn):
    query = orders.insert().values(**new_order.dict())
    last_record_id = await database.execute(query)
    return {**new_order.dict(), 'id': last_record_id}


@app.put('/orders/{order_id}', response_model=Order)
async def update_order(order_id: int, upd_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**upd_order.dict())
    await database.execute(query)
    return {**upd_order.dict(), 'id': order_id}


@app.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': f'Order ID {order_id} deleted'}

# if __name__ == '__main__':
#     uvicorn.run(app, host='172.0.0.1', port=8000)
