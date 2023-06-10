"""
Задание №7
Напишите программу на Python, которая будет находить
сумму элементов массива из 1_000_000 целых чисел.
- Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
- Массив должен быть заполнен случайными целыми числами
от 1 до 100.
- При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
- В каждом решении нужно вывести время выполнения
вычислений
"""

from random import randint
import asyncio
import time


def get_array():
    arr = [randint(1, 100) for _ in range(1, 1_000_000)]
    return arr


async def sum_async():
    sum_num = 0
    for i in get_array():
        sum_num += i
    print(f'Асинхронный подсчёт\nСумма: {sum_num}')


async def main():
    task = asyncio.create_task(sum_async())
    await task

if __name__ == '__main__':
    start_time_async = time.time()
    asyncio.run(main())
    print(f'Время выполнения: {time.time() - start_time_async:.2f} секунд')
