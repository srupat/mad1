from flask import Flask
from flask import render_template
from flask import request
import csv
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])

def data():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        id = request.form["id_value"]
        option = request.form["ID"]
        if option == "student_id":
            csv_file = "data.csv"
            with open(csv_file, 'r') as file:
                csv_reader = csv.DictReader(file)
                data_list = []
                total_marks = 0
                for row in csv_reader:
                    if row['Student id'] == id:
                        data_list.append(row)
                        total_marks+=int(row[' Marks'])
            return render_template("student.html", data_list = data_list, total_marks = total_marks)
        elif option == "course_id":
            csv_file = "data.csv"
            with open(csv_file, 'r') as file:
                csv_reader = csv.DictReader(file)
                total_marks, max_marks, count, data_list, marks = 0, 0, 0, [], []
                for row in csv_reader:
                    #print(row)
                    if int(row[' Course id']) == id:  
                        #print(row)
                        marks.append(int(row[" Marks"]))
                        data_list.append(row)
                        count += 1
                        total_marks += int(row[' Marks'])
                        if int(row[" Marks"]) > max_marks:
                            max_marks = int(row[" Marks"])
                avg_marks = total_marks / count
                plt.hist(marks, bins=10, edgecolor='black')
                plt.xlabel('Marks')
                plt.ylabel('Frequency')
                plt.savefig('histogram.png')
            return render_template("course.html", avg_marks = avg_marks, max_marks = max_marks)
    else:
        return render_template("error.html")

if __name__ == "__main__":
    app.run()