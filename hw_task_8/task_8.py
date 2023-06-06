"""
Задание №8
Создать форму для регистрации пользователей на сайте.
- Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
- При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован
"""

from flask import Flask, render_template, request, url_for, redirect
from flask_wtf.csrf import CSRFProtect
from reg_form_8 import RegistrationForm
from models_8 import Users, db
from hashlib import sha512

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_database.db'
app.config['SECRET_KEY'] = '56e641b4fe9e912f4023a6ceeb6f9a92aa9441f667b1744877401834b29dedec'
csrf = CSRFProtect(app)
db.init_app(app)
"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi user!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Users database created!')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        print(first_name, last_name, email, password)
        return fill_table(first_name, last_name, email, password)
    return render_template('register.html', form=form)


def fill_table(first_name, last_name, email, password):
    new_user = Users(first_name=first_name, last_name=last_name,
                     email=email, password=sha512(password.encode()).hexdigest())
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('good_reg'))


@app.route('/good/')
def good_reg():
    return 'Registration complite!'


@app.route('/users/')
def users():
    users_all = Users.query.all()
    context = {'users_all': users_all}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
