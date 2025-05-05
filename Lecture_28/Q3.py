import csv
values = [[7,4],[27,1,9],[1,2,3,4,5,6,7,8,9,10],[9]
with open('newcsv.csv', 'w') as myfile:
    csv_writer = csv.writer(myfile)
    for i in values:
        csv_writer.writerow(sorted(i))
