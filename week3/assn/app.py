import sys
import csv
from jinja2 import Template
import matplotlib.pyplot as plt
import pdb

TEMPLATE1 = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Data</title>
    <style> 
    table, th, td {
    border: 1px solid;
    }
    </style>
</head>
<body>
    <h1>Student Details</h1>
    <table style = "border: 1px solid;">
        <thead>
            <tr>
              <th>Student id</th>
              <th>Course id</th>
              <th>Marks</th>
          </tr>
        </thead>
        <tbody>
            
            {% for data in data_list %}
            <tr>
                <td>{{ data["Student id"] }}</td>
                <td>{{ data[" Course id"] }}</td>
                <td>{{ data[" Marks"] }}</td>
            </tr>
            {% endfor %}
            <tr>
                <td colspan = "2" style="text-align:center"> Total Marks </td>
                <td>{{ total_marks }}</td>
            </tr>
        </tbody>
    </table>
    
</body>
</html>
"""

TEMPLATE2 = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Something went wrong</title>
</head>
<body>
    <h1>Wrong Inputs</h1>
    Something Went Wrong
</body>
</html>
"""

TEMPLATE3 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Data</title>
    <style> 
    table, th, td {
    border: 1px solid;
    }
    </style>
</head>
<body>
    <h1>Course Details</h1>
    <table>
        <tr>
            <td>Average Marks</td>
            <td>Maximum Marks</td>
        </tr>
        <tr>
            <td>{{ avg_marks }}</td>
            <td>{{ max_marks }}</td>
        </tr>
        <img src="histogram.png" alt="marks histogram">
    </table>
</body>
</html>
"""

def main():
    if sys.argv[1] == "-s":
        id = sys.argv[2]
        csv_file = "data.csv"
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            data_list = []
            total_marks = 0
            for row in csv_reader:
                if row['Student id'] == id:
                    data_list.append(row)
                    total_marks+=int(row[' Marks'])
            if data_list == []:
                template = Template(TEMPLATE2)
                content = template.render(data_list = data_list, total_marks = total_marks)

                output_file = open("output.html", "w")
                output_file.write(content)
                output_file.close()
            else:
                template = Template(TEMPLATE1)
                content = template.render(data_list = data_list, total_marks = total_marks)

                output_file = open("output.html", "w")
                output_file.write(content)
                output_file.close()
    elif sys.argv[1] == "-c":
        id = int(sys.argv[2]) 
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
            plt.hist(marks, bins=10, color='blue', edgecolor='black')
            plt.xlabel('Marks')
            plt.ylabel('Frequency')
            plt.savefig('histogram.png')
            template = Template(TEMPLATE3)
            content = template.render(avg_marks=avg_marks, max_marks=max_marks)

            output_file = open("output.html", "w")
            output_file.write(content)
            output_file.close()
            

if __name__ == "__main__":
    main()
