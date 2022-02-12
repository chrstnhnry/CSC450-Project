import sys
import csv

excel_file = sys.argv[1]

matrix = []
node_names = []
unvisited = []
with open(excel_file, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, 1)
    for line in csv_reader:
        
        matrix.append(line[1:])
        node_names.append(line[0])
        unvisited.append(line[0])

def main():

    shortest_distance = [9999, 9999, 9999, 9999, 9999, 9999]

    node = input("Please, provide the source node: ")

    previous_index = [node, node, node, node, node, node]

    visited = []

    print("Shortest path tree for node " + node + ": ")

    #the index of row of node
    row = node_names.index(node)
    print(row)
    visited.append(node_names[row])
    del unvisited[row]
    for i in range(len(node_names)):
        shortest_distance[i] = int(matrix[row][i])
        

    row = shortest_distance.index(sorted(shortest_distance)[1])
    print(row)
    visited.append(node_names[row])
    del unvisited[row-1]
    for i in range(len(node_names)):
        
        cost = sum(int(matrix[row][i]), shortest_distance[row])
                   
        if (shortest_distance[i] > cost):
            shortest_distance[i] = cost

    print(visited)
    print(unvisited)
    print(node_names)
            
def sum(n1, n2):
    return n1 + n2

main()
    
