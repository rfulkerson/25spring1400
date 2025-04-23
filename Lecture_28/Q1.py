import csv
with open('mycsv.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        print(row[0])
       
# print("Hello world")
#################################
# myfile = open('mycsv.csv','r')
# 
# csv_reader = csv.reader(myfile)
# for row in csv_reader:
#     print(row[0])
# 
# myfile.close()