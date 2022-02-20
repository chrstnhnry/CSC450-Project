import csv # allows us to use and maniupulate csv files
from copy import deepcopy
import sys


#######################################################
##                    FUNCTIONS                      ##
#######################################################

# function to print out a csv file
def csvToArray(fileName):
    # open and read the file
    with open(fileName, mode="r") as csv_file: 
        reader = csv.reader(csv_file) 
        csvArray = []
        # add every item from csv file to array
        for item in reader:
            csvArray.append(item) 
    return csvArray

# function to print 2D array
# was used for debugging
def printArray2D(array):
    for x in array:
        for y in x:
            print(y, end="\t")
        print()

# function to get source node
# must take in the array made from the csv file 
# (this function is dependent on the nodes being in the first row of the csv file)
def sourceNode(nodeArray):
    node = input("Please, provide the source node: ")
    for x in nodeArray:
        # check to see if node is present in csv file
        if(str(x) == node):
            return node
    # if not, run the function again
    print("Invalid source node.")
    return sourceNode(nodeArray)   

# a function that will create a diction that says whether the nodes have been visited yet
def visitedDict(array, source):
    visitedDict = {}
    # set dictionary to all nodes unvisited
    for x in range(1, len(array[0])):
        visitedDict[array[0][x]] = False
    # make the source node visited
    visitedDict[source] = True
    return visitedDict

# a function to get just the nodes from the csv file and put them into an array
def nodeArray(array):
    ar = []
    for x in range(1, len(array[0])):
        ar.append(array[0][x])
    return ar

# a function to alphebetize a list of strings, but also have them go from shortest to longest
def alphabetize(array):
    # copy of array
    copy = []

    # set that contains all lengths of strings
    lengths = set()

    # copy the array; add lengths to the set
    for item in array:
        copy.append(item)
        lengths.add(len(item))

    # sort the list regularly
    copy.sort()

    # the list that will be returned
    final = []

    # order by length
    for length in lengths:
        for item in copy:
            if(len(item) == length):
                final.append(item)
    
    return final

# dijkstras algorithm
# takes in csv array
def dijkstra(array):
    # dictionary that contains the shortest path to each node
    # will be updated
    shortestPath = {}

    # dictionary to save the shortest currently known path to a node
    prevPath = {}

    # value set in csv file that is considered infinity
    infinity = 9999

    # get an array of all the nodes in the graph
    nodeAr = nodeArray(array)

    # since all nodes are currently unvisited, do the same command and apply to unvisited node list
    unvisitedNodes = nodeArray(array)
    
    # get the source node
    source = sourceNode(nodeAr)

    # make all shortest paths equivalent to infinity
    for node in nodeAr:
        shortestPath[node] = infinity
    
    # make the source node path = 0
    shortestPath[source] = 0

    # do the algorithm until all nodes are visited
    while unvisitedNodes:
        # node with lowest cost
        curMin = None
        for node in unvisitedNodes:
            # if there hasnt been set a lowest cost, set the first one as lowest
            if curMin == None:
                curMin = node
            # compare the shortest path of the current node to the min that we have
            elif shortestPath[node] < shortestPath[curMin]:
                curMin = node

        # retrieve the current nodes neighbors and update distances
        #get the index of the current minimum node
        indexofMin = nodeAr.index(curMin)
        # neighbors of the current node
        neighbors = {}
        # go through each neighbor in the array
        for x in range(1,len(array[indexofMin+1])):
            # make sure the neighbor isnt itself or infinity
            if(int(array[indexofMin+1][x]) != infinity and int(array[indexofMin+1][x]) != 0):
                neighbors[nodeAr[x-1]] = array[indexofMin+1][x]
        
        for neighbor in neighbors:
            tempVal = shortestPath[curMin] + int(neighbors[neighbor])
            if tempVal < shortestPath[neighbor]:
                shortestPath[neighbor] = tempVal
                # update best path to current node
                prevPath[neighbor] = curMin
        
        # after visiting all the neighbors, the node has been visited
        # can remove it from unvisited list
        unvisitedNodes.remove(curMin)
    
    # return the shortest path and revious nodes, and source node
    return shortestPath, prevPath, source

# function to clean up shortestPath and prevPath
# parameters: shortest path dict, previous node dict, array of nodes in graph, source node
def cleanOutputDijkstra(shortest, prev, nodeAr, source):
    # generate output for shortest path
    shortStr = ""
    for x in range(len(shortest)-1):
        shortStr =  shortStr + str(nodeAr[x]) + ":" + str(shortest[nodeAr[x]]) + ", "
    shortStr = shortStr + str(nodeAr[len(shortest)-1]) + ":" + str(shortest[nodeAr[len(shortest)-1]])
    
    # generate output for path taken
    prevStringAr = []
    for key in prev.keys():
        path = key
        prevNode = prev[key]
        while(prevNode != source):
            path = prevNode + path
            prevNode = prev[prevNode]
        prevStringAr.append(source + path)

    prevStringAr = alphabetize(prevStringAr)
    prevStr = ""
    for x in range(len(prevStringAr)-1):
        prevStr += prevStringAr[x] + ", "
    prevStr += prevStringAr[len(prevStringAr)-1]
    
    print(("Shortest path tree for node {}: ").format(source))
    print(prevStr)
    print(("Costs of the least-cost paths for node {}:").format(source))
    print(shortStr)

# makes a dictionary of all neighbors and their coordinates on the array from csv
def getNeighbors(source, nodeAr, array):
    infinity = 9999
    neighbors = {}
    sourceIndex = nodeAr.index(source) + 1
    for x in range(len(nodeAr)):
        if(int(array[sourceIndex][x+1]) != 0 and int(array[sourceIndex][x+1]) != infinity):
            neighbors[nodeAr[x]] = [sourceIndex,x+1]
    return neighbors

# function to perform the distance vector routing algorithm 
def dvr(array, nodeAr, source):
    # infinity value
    infinity = 9999

    # dictionary to store distances
    distances = {}
    
    # set all neighbors to infinity
    for node in nodeAr:
       distances[node] = infinity
    # set source node to 0
    distances[source] = 0

    # cycle through the algorithm num(nodes) - 1 times
    for _ in range(len(nodeAr)-1):
        # you will check each node
        for node in nodeAr:
            # get the nodes neighbors
            neighbors = getNeighbors(node, nodeAr, array)
            # analyze the neighbors
            for item in neighbors.items():
                # calculate the temporary distance 
                # item[0] is the node name (e.g. 'u', 'v', etc)
                # [item[1][row]][item[1][column]] is the row and column of a weight accroding to csv array 
                tempDist = distances[item[0]] + int(array[item[1][0]][item[1][1]])
                # if the calculated distance is less than the one in dictionary, then change it
                if tempDist < distances[node]:
                    distances[node] = tempDist
    
    # return the distances array
    return distances

# function to clean up the output of the dvr algorithm
def cleanOutputDVR(distDict, source):
    outputStr = "Distance vector for node {}: ".format(source)
    for value in distDict.values():
        outputStr += "{} ".format(value)
    print(outputStr)


# main function
def main():
    ar = csvToArray(sys.argv[1])
    nodeAr = nodeArray(ar)
    short, prev, source = dijkstra(ar)
    cleanOutputDijkstra(short, prev, nodeAr, source)
    print()
    for node in nodeAr:
        distances = dvr(ar,nodeAr,node)
        cleanOutputDVR(distances, node)


###########################################################
##                    RUNNING THE CODE                   ## 
###########################################################
main()
