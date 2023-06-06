"""
Задание №1
Создать базу данных для хранения информации о студентах университета.
- База данных должна содержать две таблицы: "Студенты" и "Факультеты".
- В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
- В таблице "Факультеты" должны быть следующие поля: id и название
факультета.
- Необходимо создать связь между таблицами "Студенты" и "Факультеты".
- Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.
"""
from random import randint, choice
from flask import Flask, render_template
from models_1 import Students, Faculties, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_database.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi, students!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Students database created!')


@app.cli.command('fill-db')
def fill_tables():
    count = 5
    for student in range(1, count + 1):
        new_student = Students(first_name=f'first_name_{student}', last_name=f'last_name_{student}',
                               age=randint(18, 40), gender=f'{choice(["m", "f"])}', group=randint(1, 6),
                               faculty_id=randint(1, 5))
        db.session.add(new_student)
    db.session.commit()
    print('Students OK')

    for faculty in range(1, count + 1):
        new_faculty = Faculties(title=f'faculty_{faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    print('Faculties OK')


@app.route('/students/')
def students_list():
    students = Students.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
