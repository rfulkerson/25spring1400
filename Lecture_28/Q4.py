import csv

file = open('output.csv', 'r')
reader = csv.reader(file)

for row in reader:
    print(row)

file.close()
