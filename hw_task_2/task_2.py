"""
Задание №2
Создать базу данных для хранения информации о книгах в библиотеке.
База данных должна содержать две таблицы: "Книги" и "Авторы".
- В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
- В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
Необходимо создать связь между таблицами "Книги" и "Авторы".
- Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.
"""

from random import randint
from flask import Flask, render_template
from models_2 import Authors, Books, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library_database.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Library database created!')


@app.cli.command('fill-db')
def fill_tables():
    count = 5
    for book in range(1, count ** 2):
        new_book = Books(title=f'title_{book}', publication_date=randint(1800, 2023),
                         copies=randint(100, 1000), author_id=randint(1, 5))
        db.session.add(new_book)
    db.session.commit()
    print('Books OK')

    for author in range(1, count + 1):
        new_author = Authors(first_name=f'first_name_{author}', last_name=f'last_name_{author}')
        db.session.add(new_author)
    db.session.commit()
    print('Authors OK')


@app.route('/')
def get_books():
    books = Books.query.all()
    context = {'books': books}
    return render_template('library.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
