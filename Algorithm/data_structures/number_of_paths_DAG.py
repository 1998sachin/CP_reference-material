# number of path between source and destination using dynamic programming, source: competitive programmer handbook
# time complexity O(E + V)
# simple graph class
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


# recursive dfs
def dfs(g, node, paths, destination):
	if node == destination:
		return 1

	if paths[node] != 0:	#using dp
		return paths[node]

	n = 0 	# to access the node see graph structure
	w = 1	# to access the weight 
	SUM = 0
	if node in g.gdict:
		for i in g.gdict[node]:
			print(node, i[0], paths)
			SUM += dfs(g, i[n], paths, destination)
	paths[node] = SUM
	return SUM
	
		
	
# sorts in topological order
def find_path_all(g, source, destination):
	paths = dict()
	
	for i in g.nodes:
		paths[i] = 0
		
	#paths[source] = 1
	return dfs(g, source, paths, destination), paths
	

	

# main starts
g = Graph()
g.addEdge(1, 2, 1, False)
g.addEdge(1, 4, 1, False)
g.addEdge(2, 3, 1, False)
g.addEdge(3, 6, 1, False)
g.addEdge(4, 5, 1, False)
g.addEdge(5, 2, 1, False)
g.addEdge(5, 3, 1, False)
#g.addEdge(2, 1, 1, False) ### this will create a cycle in the graph and dfs will run infinite time

g.display_graph()
source = 2; destination = 6
n, paths = find_path_all(g, source, destination) # n is the number of path from source to destination
print(n, paths)

