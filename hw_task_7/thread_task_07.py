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
from threading import Thread
import time


def get_array():
    arr = [randint(1, 100) for _ in range(1, 1_000_000)]
    return arr


def sum_thread():
    sum_num = 0
    for i in get_array():
        sum_num += i
    print(f'Подсчёт потоками\nСумма: {sum_num}')


threads = []
start_time_thread = time.time()
t1 = Thread(target=get_array)
threads.append(t1)
t1.start()
t2 = Thread(target=sum_thread)
threads.append(t2)
t2.start()
for t in threads:
    t.join()
print(f'Время выполнения: {time.time() - start_time_thread:.2f} секунд')
