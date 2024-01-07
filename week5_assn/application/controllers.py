from flask import Flask, request
from flask import render_template
from flask import current_app as app
from .models import Student, Course, Enrollments
from .database import db

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


