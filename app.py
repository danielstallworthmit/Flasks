from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus # To enable patch
from flask_sqlalchemy import SQLAlchemy
# import db

app = Flask(__name__)
modus = Modus(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/computers-db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/learn-flask-migrate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    excuses = db.relationship('Excuse', backref='student', lazy='dynamic')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def __repr__(self):
        return "The student's name is {} {}".format(self.first_name, self.last_name)

class Excuse(db.Model):
    __tablename__ = 'excuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    is_believable = db.Column(db.Boolean)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __init__(self, name, is_believable, student_id):
        self.name = name
        self.is_believable = is_believable
        self.student_id = student_id

class Computer(db.Model):
    __tablename__ = 'computers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    memory_in_gb = db.Column(db.Integer)

    def __init__(self, name, memory_in_gb):
        self.name = name
        self.memory_in_gb = memory_in_gb
    def __repr__(self):
        return "This {} has {} GB of memory".format(self.name, self.memory_in_gb)


@app.route('/toys',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        db.add_toy(request.form['name'])
        return redirect(url_for('index'))
    return render_template('index.html', toys=db.get_all_toys())

app.route('/toys/new')
def new():
    return render_template('new.html')

@app.route('/name/<person>', methods=["GET","POST","PATCH","DELETE"])
def hello():
    if request.method == "POST":
        # Do things
        form_list.append(Obj(request.form['firstName']))
        return redirect(url_for('index'))
    if request.method == b"PATCH":
        found.name = request.form['name']
        return redirect(url_for('index'))
    if request.method == b"DELETE":
        names.remove(found)
        return redirect(url_for('index'))
    return "Hello {person}!!!".format(person)

@app.route('/<int:id>/edit')
def edit(id):
    return render_template('edit.html', nm=found_name)

@app.route('/')
def welcome():
    names = ['D', 'J', 'J', 'F']
    random_name = 'S'
    return render_template('index.html', names=names, name=random_name)

if __name__ == "__main__":
    app.run(port=3000,debug=True)