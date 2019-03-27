# finding kth ancestor in O(log(k)) time of a node of tree, source: handbook

import queue


# simple graph class
class Graph():
    def __init__(self, mydict=None):
        if mydict == None:
            self.gdict = dict()  # for adjacency list
            self.nodes = set()  # for nodes
        else:
            self.gdict = mydict

    def addEdge(self, u, v, weight=0, bidir=False):  # bidir is False because its a tree
        self.nodes.add(u)  # adds the node u in self.nodes. O(1) on average.
        self.nodes.add(v)  # adds the node v in self.nodes

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


# returns the number of nodes
def no_of_nodes(g):
    count = 0
    for i in g.nodes:
        count += 1
    return count


# preprocessing, generates ancestor list(2d list)
def preprocessing(g, root, limit=10):
    count = no_of_nodes(g)
    ancestor = [[0 for i in range(count + 1)] for j in range(limit + 1)]  # it generates ancestors upto limit

    # processing the ancestor[1]
    visited = dict()
    for i in g.nodes:
        visited[i] = False

    q = queue.Queue()  # using queue bfs traversal
    q.put(root)

    while q.empty() == False:
        node = q.get()
        visited[node] = True
        try:
            for i in g.gdict[node]:
                if visited[i[0]] == False:  # i has form [node, weight], see the graph class
                    q.put(i[0])
                    ancestor[1][i[0]] = node
        except:
            pass

    # processing after ancestor
    for i in range(2, limit + 1):
        for j in range(count + 1):
            ancestor[i][j] = ancestor[i - 1][ancestor[i - 1][j]]

    return ancestor


# computes ancestor in O(log(k))
def find_k_ancestor(ancestor, node, k):
    if k == 1:
        return ancestor[k][node]
    else:
        if k % 2 == 0:
            value = find_k_ancestor(ancestor, node, k // 2)
            return find_k_ancestor(ancestor, value, k // 2)
        else:
            value = find_k_ancestor(ancestor, node, k // 2)
            value = find_k_ancestor(ancestor, value, k // 2)
            return find_k_ancestor(ancestor, value, 1)


# main starts
g = Graph()
g.addEdge(1, 4)
g.addEdge(1, 2)
g.addEdge(1, 5)
g.addEdge(4, 3)
g.addEdge(4, 7)
g.addEdge(7, 8)
g.addEdge(2, 6)
g.addEdge(8, 9)
g.display_graph()
ancestor = preprocessing(g, 1)
print(find_k_ancestor(ancestor, 9, 1))