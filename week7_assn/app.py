import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "week7_database.sqlite3")
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

db.session = scoped_session(db.session, scopefunc=app.app_context)
db.session.autoflush = False

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    roll_number = db.Column(db.String, unique = True, nullable= False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    course_code = db.Column(db.String, unique = True, nullable= False)
    course_name = db.Column(db.String, nullable = False)
    course_description = db.Column(db.String)

class Enrollments(db.Model):
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    estudent_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable = False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable = False)

@app.route("/")
def students():
    students = Student.query.all()
    return render_template("index.html", students = students)

@app.route("/student/create", methods = ["GET", "POST"])
def create_student():
    if request.method == "GET":
        return render_template("add_student.html")

    elif request.method == "POST":
        roll_no = request.form['roll']       
        first_name = request.form['f_name']
        last_name = request.form['l_name']
        with app.app_context():
            try:
                new_student = Student(roll_number = roll_no, first_name = first_name, last_name = last_name)
                db.session.close_all()
                db.session.add(new_student)
                db.session.commit()
            except:
                return render_template("already_exists.html")
        students = Student.query.all()
        return render_template("index.html", students = students)
    
@app.route("/student/<int:student_id>/update", methods=["GET", "POST"])
def update(student_id):
    #roll_no = request.form['roll']
    student = Student.query.get(student_id)
    # courses = Course.query.get(course_name).all()
    if request.method == "GET":        
        return render_template("update.html", student_id = student_id)
    elif request.method == "POST":
        student_id = student_id
        first_name = request.form['f_name']
        last_name = request.form['l_name']
        with app.app_context():
            try:
                student.first_name = first_name
                student.last_name = last_name            
                db.session.commit()
            except:
                return render_template("already_exists.html")
        students = Student.query.all()
        return render_template("index.html", students = students)
    
@app.route("/student/<int:student_id>/delete")
def delete(student_id):
    student = Student.query.get(student_id)
    db.session.delete(student)
    db.session.commit()
    students = Student.query.all()
    return render_template("index.html", students = students)

@app.route("/student/<int:student_id>")
def show(student_id):
    student = Student.query.get(student_id)
    enrollments = Enrollments.query.filter_by(estudent_id=student_id).all()  
    courses = [enrollment.ecourse_id for enrollment in enrollments]
    return render_template("show.html", student = student, courses=courses)




if __name__ == "__main__":
    app.debug = True
    app.run()