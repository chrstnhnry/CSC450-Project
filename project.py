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


#main()

#this is very much a work in progress 
distance = []
prev = []
class Graph:

    def __init__(self, vertices = 0):
        self.V = vertices   
        self.graph = []     

    @property
    def V(self):
        return self._V
    
    @V.setter
    def V(self, v):
        self._V = v


    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

        # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):


        dist = [9999] * self.V
        node = input("Please, provide the source node(as a number): ")
        dist[src] = int(node)
        print(self.graph)

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != 9999 and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != 9999 and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(dist)

def buildG(g):
    for i in range(len(node_names)):
        for j in range(len(node_names)):
            if(int(matrix[j][i]) != 9999):
                g.add_edge(i,j,int(matrix[j][i]))
                g.V = g.V + 1
    return g

g = Graph(5)
g = buildG(g)
g.bellman_ford(0)