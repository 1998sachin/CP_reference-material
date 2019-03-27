# topological sort using dfs, source: competitive programmer handbook

#simple graph class
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
def dfs(g, node, state, sorted_list):
	n = 0 	# to access the node see graph structure
	w = 1	# to access the weight 
	if node in g.gdict:
		for  i in g.gdict[node]:
			if state[i[n]] == 0:
				state[i[n]] = 1
				if dfs(g, i[n], state, sorted_list):
					state[i[n]] = 2
					sorted_list.append(i[n])
				else:
					return False
			elif state[i[n]] == 1:
				return False
	return True
	
# sorts in topological order
def topological_sort(g):
	state = dict()
	sorted_list = []
	for i in g.nodes:
		state[i] = 0

	for i in g.gdict:
		if state[i] == 0:
			state[i] = 1
			if dfs(g, i, state, sorted_list):
				state[i] = 2
				sorted_list.append(i)
			else:
				print("---graph has cycle----")
				return None
		
		elif state[i] == 1:
			print("----graph has cycle----")
			return None

	sorted_list.reverse()
	return sorted_list

# main starts
g = Graph()
g.addEdge('0', '1', 3, False)
g.addEdge('4', '6', 7, False)
g.addEdge('0', '2', -1, False)
g.addEdge('1', '2', 1, False)
g.addEdge('3', '4', 3, False)
g.addEdge('2', '3', 1, False)
g.addEdge('2', '5', 2, False)
g.addEdge('5', '3', 2, False)
#g.addEdge(4, 1, -2, False)

g.display_graph()
print(topological_sort(g))
