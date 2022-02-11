import sys
import csv

excel_file = sys.argv[1]

matrix = []

with open(excel_file, "r") as this_csv_file:
    csv_reader = csv.reader(this_csv_file)
    next(csv_reader, 1)
    for line in csv_reader:
        
        matrix.append(line[1:])
        
print(matrix)
