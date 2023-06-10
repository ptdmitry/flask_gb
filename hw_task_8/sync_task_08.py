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

import requests

URL_LIST = [
    'https://gb.ru/',
    'https://www.google.com/',
    'https://www.ya.ru/',
    'https://www.mail.ru/',
    'https://www.python.org/',
    'https://www.vk.com/',
]


def get_url(urls):
    for url in urls:
        u = 'sync_' + url.replace('https://', '').split('.')[-2] + '.html'
        response = requests.get(url)
        with open(u, 'w', encoding='utf-8') as f:
            f.write(response.text)


get_url(URL_LIST)
