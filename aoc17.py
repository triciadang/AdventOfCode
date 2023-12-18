#ref: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html

import sys

class Graph(object):
    def __init__(self,nodes,init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes,init_graph)

    def construct_graph(self,nodes,init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node,edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node,False)== False:
                    graph[adjacent_node][node] = value

        return graph
    
    def get_nodes(self):
        #returns graph nodes
        return self.nodes
    
    def get_outgoing_edges(self,node):
        #return node neighbors
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node,False) != False:
                connections.append(out_node)
        return connections
    
    def value(self,node1,node2):
        #return edge value between two nodes
        return self.graph[node1][node2]
    

def day17():
    f = open("input17.txt","r")
    flines = f.readlines()
    minimizeHeatLoss(flines)
    
def minimizeHeatLoss(lines):
    cityMap = []
    for i in range(0,len(lines)):
        tempArray = lines[i].strip("\n")
        tempArray = list(tempArray)
        res = [eval(i) for i in tempArray]
        lineLength = len(tempArray)
        cityMap.append(res)
    
    printArray(cityMap)

    nodes = range(0,len(cityMap)*len(cityMap[0]))

    init_graph = {}
    for node in nodes:
        init_graph[node]= {}


    for i in range(0,len(cityMap)):
        for j in range(0,len(cityMap[0])):
            firstNode = len(cityMap)*i + j

            #find all nodes with distance of 1
            k = 1
            #move 1 in each direction
            #east
            if j + k < len(cityMap[0]):
                secondNode = len(cityMap) * i + (j+k)
                init_graph[firstNode][secondNode] = cityMap[i][j+k]

            #south
            if i+ k < len(cityMap):
                secondNode = len(cityMap) * (i+k) + (j)
                init_graph[firstNode][secondNode] = cityMap[i+k][j]

            #=======================
            #find all nodes with distance of 2
                
            #2 east
            if j + 2 < len(cityMap[0]):
                secondNode = len(cityMap) * i + (j+2)
                init_graph[firstNode][secondNode]=cityMap[i][j+1] + cityMap[i][j+2]

            # east,south or south,east
            if (i+1) < len(cityMap) and (j+1) < len(cityMap[0]):
                secondNode = len(cityMap) * (i+1) + (j+1)
                dist1 = cityMap[i+1][j] + cityMap[i+1][j+1]
                dist2 = cityMap[i][j+1] + cityMap[i+1][j+1]

                if dist1 < dist2:
                    init_graph[firstNode][secondNode] = dist1
                else:
                    init_graph[firstNode][secondNode] = dist2

            # south,south
            if (i+2) < len(cityMap):
                secondNode = len(cityMap) * (i+2) +  j
                cityMap[i+1][j] + cityMap[i+2][j]

            #=======================
            # find all nodes with distance of 3
            #EEE
            if j + 3 < len(cityMap[0]):
                secondNode = len(cityMap) * i + (j+3)
                init_graph[firstNode][secondNode]=cityMap[i][j+1] + cityMap[i][j+2] +cityMap[i][j+3]



            #all for same node, 1 S, 2 E
            if (i+1) < len(cityMap) and (j+2) < len(cityMap[0]):
                secondNode = len(cityMap) * (i+1) + (j+2)
            #SEE
                dist1 = cityMap[i+1][j] + cityMap[i+1][j+1] + cityMap[i+1][j+2]
            #ESE
                dist2 = cityMap[i][j+1] + cityMap[i+1][j+1] + cityMap[i+1][j+2]
            #EES
                dist3 = cityMap[i][j+1] + cityMap[i][j+2] + cityMap[i+1][j+2]

            if(dist1 <= dist2 and dist2 <= dist3):
                init_graph[firstNode][secondNode] = dist1
 
            elif(dist2 <= dist1 and dist2 <= dist3):
                init_graph[firstNode][secondNode] = dist2
            else:
                init_graph[firstNode][secondNode] = dist3
            

            #all fo same node, 2 S, 1 E
            if (i+2) < len(cityMap) and (j+1) < len(cityMap[0]):
                secondNode = len(cityMap) * (i+2) + (j+1)

            #SSE
                dist1 = cityMap[i+1][j] + cityMap[i+2][j] + cityMap[i+2][j+1]
            #SES
                dist2 = cityMap[i+1][j] + cityMap[i+1][j+1] + cityMap[i+2][j+1]
            #ESS
                dist3 = cityMap[i][j+1] + cityMap[i+1][j+1] + cityMap[i+2][j+1]

            if(dist1 <= dist2 and dist2 <= dist3):
                init_graph[firstNode][secondNode] = dist1
            elif(dist2 <= dist1 and dist2 <= dist3):
                init_graph[firstNode][secondNode] = dist2
            else:
                init_graph[firstNode][secondNode] = dist3
            
            #SSS
            if i + 3 < len(cityMap):
                secondNode = len(cityMap) * (i+3) + (j)
                init_graph[firstNode][secondNode]=cityMap[i+1][j] + cityMap[i+2][j] +cityMap[i+3][j]


    print(init_graph)
    graph = Graph(nodes,init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=0)

    print_result(previous_nodes, shortest_path, start_node=0, target_node=168)
	
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path




def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(path)

def printArray(array):
    for each in array:
        print(each)

day17()