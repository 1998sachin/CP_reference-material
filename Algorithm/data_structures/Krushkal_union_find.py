# Krushkal's implementation
# union find structure, source: competitive handbook


# a simple graph class
class Graph:
    def __init__(self, mydict=None):
        if mydict == None:
            self.gdict = dict()
        else:
            self.gdict = mydict

    def addEdge(self, u, v, weight=0, bidir=True):
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


# creates a size dictionary where size[i] = 1 (i being the node).
# Size will be used as rank of the node
def create_size(g):
	size = dict()
	for i in g.gdict:
		size[i] = 1
	return size


# creates a link dictionary that will serve as the representative of the set.
def create_link(g):
	link = dict()
	for i in g.gdict:
		link[i] = i
	return link


# find function, it returns the link of node i
def find(node, link):
	while link[node] != node:
		node = link[node]
	return node


# same function checks if two nodes belong to the same set or not
def same(a, b, link):
	return find(a, link) == find(b, link)


# unite function joins two set
def unite(a, b, link, size):
	a = find(a, link)
	b = find(b, link)

	if size[a] < size[b]:
		size[b] += size[a]
		link[a] = b
	else:
		size[a] += size[b]
		link[b] = a
	return


# to get the edgelist of the graph. Time complexity is O(E*V).
# This part is optional. It is there for maximum compatibility
# One can directly creates an edge list at the time of input
def get_edgelist(g):
	n = 0 	# to access the node (see the graph structure)
	w = 1 	# to access the weight of the node
	
	visited = dict()
	edgeList = []
	for i in g.gdict:
		visited[i] = False
	
	for i in g.gdict:
		for j in g.gdict[i]:
			if visited[j[n]] == False:
				edgeList.append([i, j[n], j[w]])
		visited[i] = True		

	return edgeList


# returns the weight of minimum spanning tree
def krushkal_span(edgeList, link, size):
	edgeList = sorted(edgeList, key=lambda l:l[2])  # sorting edgeList according to the weight in non 
	# decresing order

	total_min_weight = 0
	for i in edgeList:
		if same(i[0], i[1], link) == False:
			unite(i[0], i[1], link, size)
			total_min_weight += i[2]
	return total_min_weight


# main starts
g = Graph()
g.addEdge(0, 1, 3)
g.addEdge(0, 2, -1)
g.addEdge(1, 2, 1)
g.addEdge(3, 4, 3)
g.addEdge(2, 3, 1)
g.addEdge(4, 1, -5)
g.display_graph()

link = create_link(g)
size = create_size(g)

edgeList = get_edgelist(g)

total_min_weight = krushkal_span(edgeList, link, size)
print(total_min_weight)
