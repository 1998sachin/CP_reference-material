# implementation of Prim's algorithm using heapdict (heap + dictionary), source: Tushar Roy, YouTube.

from heapdict import heapdict


# simple graph class
class Graph:
    def __init__(self, mydict=None):
        if mydict == None:
            self.gdict = dict()
        else:
            self.gdict = mydict

    def addEdge(self, u, v, weight = 0, bidir = True):
        if u in self.gdict:
            self.gdict[u].append([v, weight])
        else:
            self.gdict[u] = [[v, weight]]

        if bidir == True:
            if v in self.gdict:
                self.gdict[v].append([u, weight])
            else:
                self.gdict[v] = [[u, weight]]
    def display_graph(self):
        print(self.gdict)


# function implementing prims algorithm
def prims_span(g, arbitrary_source):
    visited = dict()
    minEdge = heapdict()    # serve as map + binary heap 
    minSpanTree = dict()    # edge description for spanning tree

    for i in g.gdict:
        visited[i] = False
        minEdge[i] = float('inf')

    minEdge[arbitrary_source] = 0
    total_min_weight = 0    # weight of the entire spanning tree

    while len(minEdge) != 0:
        node, weight = list(minEdge.popitem())  # popitem() returns a tuple (node, distance)
        total_min_weight += weight
                
        for i in g.gdict[node]:  # i has structure [node, weight] (see the graph structure)
            if i[0] in minEdge and i[1] < minEdge[i[0]] and visited[i[0]] == False:
                minEdge[i[0]] = i[1]
                minSpanTree[i[0]] = node    # storing the information about edges in min spanning tree
        visited[node] = True
    
    return minSpanTree, total_min_weight


# main starts
g = Graph()
g.addEdge(0, 1, 3)
g.addEdge(0, 2, -1)
g.addEdge(1, 2, 1)
g.addEdge(3, 4, 3)
g.addEdge(2, 3, 1)
#g.addEdge(4, 1, -5)
g.display_graph()

minSpanTree, total_min_weight = prims_span(g, 0)  # 0 is the arbitrary source
print(minSpanTree)
print(total_min_weight)