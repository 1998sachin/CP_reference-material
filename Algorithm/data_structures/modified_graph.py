# It creates dictionary instead of list for a node to represent adjacency list, it is useful for duplicate edges
# It assigns minimum weight to the edge.
from heapdict import heapdict

class Graph():
    def __init__(self, mydict=None):
        if mydict == None:
            self.gdict = dict()
        else:
            self.gdict = mydict

    def addEdge(self, u, v, weight, bidir = True):
        if u in self.gdict:
            if v in self.gdict[u]:
                self.gdict[u][v] = min(self.gdict[u][v], weight)
            else:
                self.gdict[u][v] = weight
        else:
            self.gdict[u] = {v: weight}

        if bidir == True:
            if v in self.gdict:
                if u in self.gdict[v]:
                    self.gdict[v][u] = min(self.gdict[v][u], weight)
                else:
                    self.gdict[v][u] = weight
            else:
                self.gdict[v] = {u : weight}
    def display_graph(self):
        print(self.gdict)

def dijkstra(g, source):
    parent = dict() # for tracing the path
    distance = dict()    # for storing the minimum distances
    visited = dict()    # for checking if node is already discovered
    dis = heapdict()    # works heap and dictionary
    for i in g.gdict:
        parent[i] = -1
        visited[i] = False
        distance[i] = float("inf")
        dis[i] = float("inf")

    distance[source] = 0
    dis[source] = 0

    while len(dis) != 0:
        node = list(dis.popitem())[0]  #popitem() returns a tuple (node, distance)
        visited[node] = True    #marking it as visited
        for j in g.gdict[node]: # j has form [node, weight] i.e j[0] is node and j[1] is weight
            if (distance[node] + g.gdict[node][j] < distance[j]) and visited[j] == False:
                distance[j] = distance[node] + g.gdict[node][j]
                dis[j] = distance[node] + g.gdict[node][j]
                parent[j] = node
    print(distance)
    print(parent)

g  = Graph()
g.addEdge('A', 'B', 5)
g.addEdge('A', 'B', 1)
g.addEdge('A', 'E', 2)
g.addEdge('A', 'D', 9)
g.addEdge('B', 'C', 2)
g.addEdge('C', 'D', 3)
g.addEdge('D', 'F', 2)
g.addEdge('E', 'F', 3)
g.display_graph()
dijkstra(g, 'A')