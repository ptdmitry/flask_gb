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
import time


def get_array():
    arr = [randint(1, 100) for _ in range(1, 1_000_000)]
    return arr


def sum_sync():
    sum_num = 0
    start_time_sync = time.time()
    for i in get_array():
        sum_num += i
    return f'Синхронный метод.\nСумма: {sum_num} ' \
           f'за {time.time() - start_time_sync:.2f} секунд'


if __name__ == '__main__':
    print(sum_sync())
