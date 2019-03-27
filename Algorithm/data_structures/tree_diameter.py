# calculates the diameter of tree in O(n) time complexity

# general graph class. This can be used to represent tree
class Graph():
    def __init__(self, mydict=None):
        if mydict == None:
            self.gdict = dict()
        else:
            self.gdict = mydict

    def addEdge(self, u, v, weight = 1, bidir = True):
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

def diameter(g, current, source, toLeaf = dict(), maxLength = dict()):
	node = 0
	weight = 1
	toLeaf[current] = -1
	maxLength[current] = -1
	first = current
	second = current
	for i in g.gdict[current]:
		if i[node] != source:
			diameter(g, i[node], current, toLeaf, maxLength)
			if toLeaf[i[node]] >= toLeaf[first]:
				second = first
				first = i[node]
			else:
				if toLeaf[second] < toLeaf[i[node]]:
					second = i[node]

	maxLength[current] = toLeaf[first] + toLeaf[second] + 2
	toLeaf[current] = 1 + toLeaf[first]
	
	return maxLength

# main starts
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(4, 6)
g.addEdge(3, 7)
g.addEdge(7, 9)
g.addEdge(4, 6)
g.addEdge(6, 8)
g.display_graph()

maxLength = diameter(g, 0, -1)
dia = -1
for i,j in maxLength.items():
	dia = max(dia, j)
print(dia)

