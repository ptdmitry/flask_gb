"""
Задание №9
Создать страницу, на которой будет форма для ввода имени
и электронной почты
- При отправке которой будет создан cookie файл с данными
пользователя
- Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
- На странице приветствия должна быть кнопка "Выйти"
- При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""

from flask import Flask, request, render_template, url_for, make_response

app = Flask(__name__)


@app.get('/hello/<username>/')
def hello_get(username):
    return render_template('hello_9.html', username=username)


@app.get('/')
def cookie_get():
    return render_template('cookie.html')


@app.post('/submit')
def cookie_post():
    username = request.form.get('name')
    user_email = request.form.get('email')
    response = make_response(render_template('hello_9.html'))
    response.set_cookie('username', username)
    response.set_cookie('user_email', user_email)
    return response


@app.post('/logout/')
def logout_post():
    response = make_response(url_for('cookie_get'))
    response.delete_cookie('username')
    response.delete_cookie('user_email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
