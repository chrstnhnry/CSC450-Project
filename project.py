import sys
import csv

excel_file = sys.argv[1]

matrix = []
node_names = []

with open(excel_file, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, 1)
    for line in csv_reader:
        
        matrix.append(line[1:])
        node_names.append(line[0])

node = input("Please, provide the source node: ")

def main():
    
#cost between two nodes that are given
def cost(n1, n2):
    
