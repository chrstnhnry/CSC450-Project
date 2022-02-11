import sys
import csv

excel_file = sys.argv[1]

with open(excel_file, "r") as this_csv_file:
    this_csv_reader = csv.reader(this_csv_file, delimiter=",")
    header = next(this_csv_reader)
    print(header)
