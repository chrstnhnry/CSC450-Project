import sys
import csv

excel_file = sys.argv[1]
row_cost = []
total_cost_list = []
matrix = []
node_names = []
unvisited = []
visited = []
previous_index = []
shortest_distance = [9999, 9999, 9999, 9999, 9999, 9999]

with open(excel_file, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, 1)
    for line in csv_reader:
        
        matrix.append(line[1:])
        node_names.append(line[0])
        unvisited.append(line[0])

def main2():

    current_vertex = node_names.index(node)
    previous_vertex = current_vertex

    #row
    for i in range(len(node_names)):
        
        visited.append(current_vertex)
        unvisited.remove(node_names[current_vertex])
        
        #column
        for j in range(len(node_names)):
            
            if int(matrix[current_vertex][j] < 9999:
                total_cost = totalCost(current_vertex, previous_vertex, j, visited)
                   
            else:
                total_cost = 9999
                
            row_cost.append(total_cost)
            
            if total_cost < shortest_distance[j]:
                shortest_distance[i] = total_cost
        
        previous_vertex = current_vertex
                   
        #set current vertex
        while True:
            
            if visited.count(row_cost.index(min(a))) > 0:
                current_vertex = row_cost.index(min(a))
                break
        
            else:
                row_cost.index(min(a)) = 9999

        #clear row total cost
        row_cost.clear()
        

def totalCost(current_vertex, previous_vertex, j, visited):
    if len(visited) == 1:
        return int(matrix[current_vertex][j])

    else:
        return int(matrix[][]) + totalCost(curent_vertex, previous_vertex, j, )











def main():

    node = input("Please, provide the source node: ")

    print("Shortest path tree for node " + node + ": ")
    
    current_vertex = node_names.index(node)
    previous_vertex = 0
    
    for i in range(len(node_names)):
        
        total_cost = int(matrix[current_vertex][i]) + int(matrix[current_vertex][current_vertex])
        total_cost_list.append(total_cost)
        
        if total_cost < shortest_distance[i]:
            shortest_distance[i] = total_cost

    previous_vertex = current_vertex
    current_vertex = shortest_distance.index(sorted(total_cost_list)[1])

    print(shortest_distance)

    for i in range(len(node_names)):

        total_cost = int(matrix[current_vertex][i]) + int(matrix[previous_vertex][current_vertex])
        if total_cost < shortest_distance[i]:
            shortest_distance[i] = total_cost
    
    previous_vertex = current_vertex
    current_vertex = 1

    print(shortest_distance)

    for i in range(len(node_names)):

        total_cost = int(matrix[current_vertex][i]) + int(matrix[previous_vertex][current_vertex]) + int(matrix[0][previous_vertex])
        if total_cost < shortest_distance[i]:
            shortest_distance[i] = total_cost

    previous_vertex = current_vertex
    current_vertex = 4

    print(shortest_distance)

    for i in range(len(node_names)):

        total_cost = int(matrix[current_vertex][i]) + int(matrix[previous_vertex][current_vertex]) + int(matrix[0][2]) + int(matrix[2][previous_vertex])
        if total_cost < shortest_distance[i]:
            shortest_distance[i] = total_cost
            
    print(shortest_distance)
    

main()
    
