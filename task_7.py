"""
Задание №7
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
"""

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/square_number/<num>/')
def square_number(num):
    return f'Число {num} в квадрате: {int(num) ** 2}'


@app.get('/num/')
def age_get():
    return render_template('number.html')


@app.post('/num/')
def age_post():
    num = int(request.form.get('num'))
    return redirect(url_for('square_number', num=num))


if __name__ == '__main__':
    app.run(debug=True)
