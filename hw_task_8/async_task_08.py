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

import asyncio
import aiohttp

URL_LIST = [
    'https://gb.ru/',
    'https://www.google.com/',
    'https://www.ya.ru/',
    'https://www.mail.ru/',
    'https://www.python.org/',
    'https://www.vk.com/',
]


async def get_page(got_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(got_url) as response:
            u = 'async_' + got_url.replace('https://', '').split('.')[-2] + '.html'
            text = await response.text()
            with open(u, 'w', encoding='utf-8') as f:
                f.write(text)


async def main():
    tasks = []
    for url in URL_LIST:
        task = asyncio.ensure_future(get_page(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
