# Python graph 
# Graphs are implemented as dictionary of lists, where key represent node, value represents edges from that node
# It is essentially adjacency list representation of graph

class Graph:
    # creates a dictionay (graph)
    def __init__(self, gdict=None):
        if gdict == None:
            gdict = {}
        self.gdict = gdict

    # returns the keys of the dictionary(nodes of the graph)
    def getVertices(self):
        return list(self.gdict.keys())

    # adds a key(vertex) to the dictionary(graph)
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    # adds an edge to the vertex of the graph. Edge is of the form (vrtx_1, vrtx_2),
    # bidir tells if the graph is bi directional
    def addEdge(self, vrtx_1, vrtx_2, bidir = True):
        if vrtx_1 in self.gdict:
            self.gdict[vrtx_1].append(vrtx_2)
        else:
            self.gdict[vrtx_1] = [vrtx_2]

        if bidir == True:  # if it is bi-directional graph
            if vrtx_2 in self.gdict:
                self.gdict[vrtx_2].append(vrtx_1)
            else:
                self.gdict[vrtx_2] = [vrtx_1]

    # prints the whole graph
    def displayGraph(self):
        for key in self.gdict:
            print(key, '->', end=' ')
            print(self.gdict[key])

    # breadth first search
    def bfs(self, source, destination):

        visited = [False] * len(self.gdict)
        distance = [0] * len(self.gdict)
        parent = [-1] * len(self.gdict)

        queue = []  # using list as queue
        queue.insert(0, source)
        visited[source] = True

        while len(queue) != 0:
            node = queue.pop()
            neighbours = self.gdict[node]
            for i in neighbours:
                if visited[i] == False:
                    queue.insert(0, i)
                    visited[i] = True
                    distance[i] = distance[node] + 1
                    parent[i] = node
                    print(node, end=" ")

        print("\nshortest path from %d to %d" % (source, destination))

        temp = destination
        while True:
            print(temp, "<-", end=' ')
            if temp == source:
                break
            temp = parent[temp]

    def dfs(self, source):
        visited = [False] * len(self.gdict)
        stack = [] #this will be used as stack
        stack.append(source)
        self.dfs_recur(source, stack, visited)

    def dfs_recur(self, source, stack = [], visited = []):
        if len(stack) == 0:
            return
        node = stack.pop()
        visited[node] = True
        print(node, end=' ')
        neighbours = self.gdict[node]
        for i in neighbours:
            if visited[i] == False:
                stack.append(i)
                self.dfs_recur(i, stack, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(0, 4)
g.addEdge(2, 4)
g.addEdge(3, 2)
g.addEdge(3, 5)
g.addEdge(3, 4)

g.displayGraph()
#g.bfs(1, 3)
g.dfs(0)
