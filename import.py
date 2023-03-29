import csv
with open("SalesJan2009") as csvfile:
     reader = csv.DictReader(csvfile)
     
     for row in reader:
         print(row[0], row[1])
         print(row)