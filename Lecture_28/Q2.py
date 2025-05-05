import csv
grades = {}
with open('mycsv.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        if row[1].isdecimal():
            grades[row[0]] = int(row[1]) + int(row[2]) + int(row[3])
print(grades['Padma'])
print(grades['Will'])


