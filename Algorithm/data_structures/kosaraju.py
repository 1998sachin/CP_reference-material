# implementation of kosaraju's alogrithm, source: Tushar Roy YouTube/kosaraju

import queue #for stack data structure

# simple graph class
# can handle weighted, unweighted, directed, undirected, nodes can be string also
class Graph():
    def __init__(self, mydict=None):
        if mydict == None:
            self.gdict = dict() # for adjacency list
            self.nodes = set()  # for nodes
        else:
            self.gdict = mydict

    def addEdge(self, u, v, weight = 0, bidir = False):
        self.nodes.add(u)   # adds the node u in self.nodes. O(1) on average.
        self.nodes.add(v)   # adds the node v in self.nodes

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

# for phase 1
def dfs_1(g, node, visited, mystack):
    if node in g.gdict:
        for i in g.gdict[node]:
            if visited[i[0]] == False:   # i has form [node, weight], see the graph structure
                visited[i[0]] = True
                dfs_1(g, i[0], visited, mystack)
        mystack.put(node)

    else:
        mystack.put(node)


# reverses all the edges of a directed graph
def reverse_all_edges(g):
    aux = Graph() # auxiliary graph (reversed edges of g)

    for node in g.gdict:
        for i in g.gdict[node]:
            aux.addEdge(i[0], node) # i has form [node, weight], see the graph structure

    return aux

# for phase 2
def dfs_2(g, node, visited, part):
    if node in g.gdict:
        for i in g.gdict[node]:
            if visited[i[0]] == False:  # i has form [node, weight], see the graph structure
                visited[i[0]] = True
                part.append(i[0])
                dfs_2(g, i[0], visited, part)

# returns the list of connected components
def kosaraju_strong_comp(g):
    visited = dict()
    for i in g.nodes:
        visited[i] = False

    mystack = queue.LifoQueue()  # works as stack

    # phase 1
    for i in g.nodes:
        if visited[i] == False:
            visited[i] = True
            dfs_1(g, i, visited, mystack)

    # phase 2
    # reversal of edges
    g = reverse_all_edges(g)
    scomponents = [] # it contains the connected components, (list of list)

    # forming the strongly connected components
    for i in g.nodes:
        visited[i] = False

    while mystack.qsize() > 0:
        node = mystack.get()
        part = []   # contains one connected component
        if visited[node] == False:
            visited[node] = True
            part.append(node)
            dfs_2(g, node, visited, part)
            scomponents.append(part)

    return scomponents

# main starts
g = Graph()
g.addEdge('A', 'B')
g.addEdge('C', 'A')
g.addEdge('B', 'C')
g.addEdge('B', 'D')
g.addEdge('D', 'E')
g.addEdge('E', 'F')
g.addEdge('F', 'D')
g.addEdge('G', 'F')
g.addEdge('G', 'H')
g.addEdge('H', 'I')
g.addEdge('I', 'J')
g.addEdge('J', 'G')
g.addEdge('J', 'K')

g.display_graph()
print(kosaraju_strong_comp(g))