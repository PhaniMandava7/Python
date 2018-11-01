import csv

with open('C:/Users/Phani/Desktop/names.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader:
        print(line)