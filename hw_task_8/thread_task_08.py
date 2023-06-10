"""
Задание №8
Напишите программу, которая будет скачивать страницы из
списка URL-адресов и сохранять их в отдельные файлы на
диске.
- В списке может быть несколько сотен URL-адресов.
- При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
- Представьте три варианта решения.
"""

from threading import Thread
import requests

URL_LIST = [
    'https://gb.ru/',
    'https://www.google.com/',
    'https://www.ya.ru/',
    'https://www.mail.ru/',
    'https://www.python.org/',
    'https://www.vk.com/',
]


def get_page(got_url):
    u = 'thread_' + got_url.replace('https://', '').split('.')[-2] + '.html'
    response = requests.get(got_url)
    with open(u, 'w', encoding='utf-8') as f:
        f.write(response.text)


threads = []
for url in URL_LIST:
    t = Thread(target=get_page, args=(url, ))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
