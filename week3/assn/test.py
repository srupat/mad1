import csv

csv_file = "data.csv"
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)


print(data_list)