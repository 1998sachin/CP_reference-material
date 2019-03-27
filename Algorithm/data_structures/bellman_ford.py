class Graph:
    def __init__(self, gdict = None):
        if gdict == None:
            self.gdict = dict()
        else:
            self.gdict = gdict

    def addEdge(self, u, v, weight = 1, bidir = False):
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


def bellman_ford(g, n, source): # n is the number of nodes
    parent = dict()     #contains the parent of i
    distance = dict()   #contains the minimum distance from source
    for i in range(0, n):
        parent[i] = -1
        distance[i] = float('inf')

    distance[source] = 0    #setting the distance of source to be zero

    # loop n - 1 times for shortest path from the source
    for _ in range(n-1):
        for i in g.gdict:
            for j in g.gdict[i]:
                relax(i, j, parent, distance)

    # to detect a negative cycle:
    for i in g.gdict:
        for j in g.gdict[i]:
            if relax(i, j, parent, distance):
                print("has a negative cycle")
                return
    else:
        print("does not have a negative cycle")


def relax(u, v, parent, distance, node=0, weight=1):

    if distance[u] + v[weight] < distance[v[node]] and distance[u] + v[weight] < 10 ** 10:   # dealing with infinity
        distance[v[node]] = distance[u] + v[weight]
        parent[v[node]] = u
        return 1
    else:
        return 0


# main starts
g = Graph()
g.addEdge(0, 1, 1)
g.addEdge(1, 2, -2)
g.addEdge(2, 3, 1)
g.addEdge(3, 1, -3)

g.display_graph()
bellman_ford(g, 4, 3)
