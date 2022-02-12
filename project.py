import sys
import csv

excel_file = sys.argv[1]

matrix = []
node_names = []
unvisited = []
visited = []
previous_index = ['', '', '', '', '', '']
shortest_distance = [9999, 9999, 9999, 9999, 9999, 9999]

with open(excel_file, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, 1)
    for line in csv_reader:
        
        matrix.append(line[1:])
        node_names.append(line[0])
        unvisited.append(line[0])

def main():

    node = input("Please, provide the source node: ")

    print("Shortest path tree for node " + node + ": ")

    current_vertex = node_names.index(node)
    previous_vertex = 0
    for i in range(len(node_names)):
        if int(matrix[current_vertex][i]) < 9999:
            total_cost = int(matrix[current_vertex][i]) + int(matrix[previous_vertex][previous_vertex])
            if total_cost < shortest_distance[i]:
                shortest_distance[i] = total_cost

    previous_vertex = current_vertex
    current_vertex = shortest_distance.index(sorted(shortest_distance)[1])

    print(previous_vertex)
    print(current_vertex)
    
    for i in range(len(node_names)):
        if int(matrix[current_vertex][i]) < 9999:
            total_cost = int(matrix[current_vertex][i]) + int(matrix[previous_vertex][current_vertex])
            if total_cost < shortest_distance[i]:
                shortest_distance[i] = total_cost

    print(shortest_distance)

main()
    
