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
from multiprocessing import Process, Value
import time

sum_num = Value('i', 0)


def get_array():
    arr = [randint(1, 100) for _ in range(1, 1_000_000)]
    return arr


def sum_process(array):
    for i in get_array():
        with array.get_lock():
            sum_num.value += i
    print(f'Подсчёт процессами\nСумма: {sum_num.value}')


processes = []

if __name__ == '__main__':
    start_time_process = time.time()
    p1 = Process(target=get_array)
    processes.append(p1)
    p1.start()
    p2 = Process(target=sum_process(sum_num))
    processes.append(p2)
    p2.start()
    for p in processes:
        p.join()
    print(f'Время выполнения: {time.time() - start_time_process:.2f} секунд')
