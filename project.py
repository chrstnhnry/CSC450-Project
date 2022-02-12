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

def main():

    shortest_distance = [9999, 9999, 9999, 9999, 9999, 9999]

    node = input("Please, provide the source node: ")

    previous_index = [node, node, node, node, node, node]

    print("Shortest path tree for node " + node + ": ")

    #the index of row of node
    row = node_names.index(node)

    for i in range(len(node_names)):
        shortest_distance[i] = cost(shortest_distance[i], int(matrix[row][i]))

    print(sorted(shortest_distance)[1])
    
    print(shortest_distance)
    print(previous_index)
        

    

#cost between two nodes that are given
def cost(n1, n2):
    if n1 > n2:
        return n2
    else:
        return n1

main()
    
