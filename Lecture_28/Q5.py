import csv
data = [['name', 'age'], 
    ['Alice', 30], 
    ['Bob', 25]]
with open('output.csv', 'w') as file:
    writer = csv.writer(file, delimiter=':')
    writer.writerows(data)

