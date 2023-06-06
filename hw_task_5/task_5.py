"""
Задание №5
Создать форму регистрации для пользователя.
- Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением),
дата рождения, согласие на обработку персональных данных.
- Валидация должна проверять, что все поля заполнены корректно
(например, дата рождения должна быть в формате дд.мм.гггг).
- При успешной регистрации пользователь должен быть перенаправлен
на страницу подтверждения регистрации.
"""

from flask import Flask, render_template, request, url_for, redirect
from flask_wtf.csrf import CSRFProtect
from reg_form_5 import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '0b7fcf284aa6c733b5dcba52620c6c7ce4bcb2fd1639581dac69004f50f2f0b8'
csrf = CSRFProtect(app)
"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        return redirect(url_for('good_reg'))
    return render_template('register.html', form=form)


@app.route('/good/')
def good_reg():
    return 'Registration complite!'


if __name__ == '__main__':
    app.run(debug=True)
