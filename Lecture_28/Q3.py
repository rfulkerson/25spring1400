import csv
values = [[7,4],[27,1,9],[7],[2345,2345,234,5234,523,4523,4562345,6]]
with open('newcsv.csv', 'w') as myfile:
    csv_writer = csv.writer(myfile)
    for i in values:
        csv_writer.writerow(sorted(i))
