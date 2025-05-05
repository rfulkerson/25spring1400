import csv
with open('mycsv.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile)
    first = True
    for row in csv_reader:
        if first == True:
            first = False
            continue
        print(row[0])
       
#################################
# myfile = open('mycsv.csv','r')
# # 
# csv_reader = csv.reader(myfile)
# for row in csv_reader:
#     print(row[0])
# # 
# myfile.close()