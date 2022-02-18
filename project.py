import sys
import csv
from turtle import distance
from urllib.parse import _NetlocResultMixinStr

excel_file = sys.argv[1]
row_cost = []
total_cost_list = []
matrix = []
node_names = []
unvisited = []
visited = []
visitedCheck = [0,0,0,0,0,0]
previous_index = []
shortest_distance = [9999, 9999, 9999, 9999, 9999, 9999]
node = ""

with open(excel_file, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, 1)
    for line in csv_reader:
        
        matrix.append(line[1:])
        node_names.append(line[0])
        unvisited.append(line[0])

def main():
    
    node = input("Please, provide the source node: ")
    current_vertex = node_names.index(node)
    previous_vertex = current_vertex
    visited.append(current_vertex)
    #visitedCheck[current_vertex] = 9999
    
    #row
    for i in range(len(node_names)):

        #unvisited.remove(node_names[current_vertex])
        #column
        for j in range(len(node_names)):
            
            if int(matrix[current_vertex][j]) < 9999:
                total_cost = totalCost(current_vertex, previous_vertex, j, visited)
                print("total cost: " + str(total_cost))
            else:
                total_cost = 9999
                
            row_cost.append(total_cost)
            
            if total_cost < shortest_distance[j]:
                shortest_distance[j] = total_cost
        
        previous_vertex = current_vertex
        
        #set current vertex
        i = 0
        while i < 1:
            print("row cost:" + str(row_cost))
            print(row_cost.index(min(row_cost)))
            print("Visited Check: " + str(visitedCheck))
            print("Visited: " + str(visited))
            if ((visited.count(row_cost.index(min(row_cost))) < 1) & (visitedCheck[row_cost.index(min(row_cost))] != 9999)):
                current_vertex = row_cost.index(min(row_cost))
                print("current vertex: " + str(current_vertex))
                #row_cost[row_cost.index(min(row_cost))] = 9999
                visitedCheck[row_cost.index(min(row_cost))] = 9999
                i+=1

            else:
                if visitedCheck == [9999,9999,9999,9999,9999,9999]:
                    i+=1
                visitedCheck[row_cost.index(min(row_cost))] = 9999
                row_cost[row_cost.index(min(row_cost))] = 9999
                
        visited.append(current_vertex)
        print("visited: " + str(visited))
        #clear row total cost
        row_cost.clear()

        print("shortest distance: " + str(shortest_distance))
        

def totalCost(current_vertex, previous_vertex, j, poggers):
    #print("VISITED: " + str(poggers))

    if len(poggers) == 1:
        return int(matrix[current_vertex][j])

    elif len(poggers) == 2:
        return int(matrix[current_vertex][j]) + int(matrix[previous_vertex][current_vertex])
    
    else:
        a = poggers[0]
        b = poggers[1]
        return int(matrix[a][b]) + totalCost(current_vertex, previous_vertex, j, poggers[1:])


main()

#this is very much a work in progress 
distance = []
prev = []
class Graph:

    def __init__(self, vertices = 0):
        self.V = vertices   
        self.graph = []     

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def bellamnFord():
        for vertex in matrix:
            distance.append(9999)
            prev.append(None)
        current_vertex = node_names.index(node)
        distance[current_vertex] = 0

    def bellman_ford(self, src):

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist)

def buildG(g):
    for i in matrix:
        for j in i:
            print (i)
            if(int(matrix[i][j]) != 9999):
                g.add_edge(i[j],j,matrix[i[j]][j])
                g.vertices = g.vertices + 1
    return g

g = Graph()
#g = buildG(g)
#g.bellamnFord(0)