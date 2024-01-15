import csv
from io import StringIO
data = """Date,Value1,Value2
2021-01-01,10,20
2021-01-02,15,25
2021-01-03,20,30
"""
file = StringIO(data)
for row in csv.reader(file):
    if row:
        print(row[1])