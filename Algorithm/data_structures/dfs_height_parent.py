# dfs algorithm for height and parent

class Graph():
	def __init__(self, mydict=None):
		if mydict == None:
			self.gdict = dict() # for adjacency list
			self.nodes = set()	# for nodes
		else:
			self.gdict = mydict

	def addEdge(self, u, v, weight = 0, bidir = True):
		self.nodes.add(u) 	# adds the node u in self.nodes. O(1) on average.
		self.nodes.add(v)	# adds the node v in self.nodes

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

def dfs(g, node, height, parent, visited):
	if node in g.gdict:
		for i in g.gdict[node]:
			if visited[i[0]] == False:
				visited[i[0]] = True
				parent[i[0]] = node
				dfs(g, i[0], height, parent, visited)

		h =  -float('inf')
		for i in g.gdict[node]:
			h = max(h, height[i[0]])

		height[node] = 1 + h

	
def myfunction(g, n, source):
	parent = dict()
	height = dict()
	visited = dict()
	for i in g.nodes:
		parent[i] = -1
		height[i] = -1
		visited[i] = False
	visited[source] = True
	dfs(g, source, height, parent, visited)
	return height, parent
