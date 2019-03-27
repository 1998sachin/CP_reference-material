#simple graph class
class Graph():
    def __init__(self, mydict=None):
        if mydict == None:
            self.gdict = dict() # for adjacency list
            self.nodes = set()  # for nodes
        else:
            self.gdict = mydict

    def addEdge(self, u, v, weight = 0, bidir = True):
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