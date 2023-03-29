import csv
with open("SalesJan2009.csv", "r") as f:
    reader = csv.DictReader(f)
    a = dict(reader)
    print (a)