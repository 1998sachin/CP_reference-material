# implementation of Dijkstra's shortest path algorithm
# in O(Elog(V)) time complexity using heapdict

from heapdict import heapdict
from simple_graph_class import Graph  # class for graph


def dijkstra(g, source):
	parent = dict()  # for tracing the path
	distance = dict()  # for storing the minimum distances
	visited = dict()  # for checking if node is already discovered	
	dis = heapdict()  # works heap and dictionary
	for i in g.gdict:
		parent[i] = -1
		visited[i] = False
		distance[i] = float("inf")
		dis[i] = float("inf")

	distance[source] = 0
	dis[source] = 0

	while len(dis) != 0:
		node = list(dis.popitem())[0]  # popitem() returns a tuple (node, distance)
		visited[node] = True	# marking it as visited
		for j in g.gdict[node]: # j has form [node, weight] i.e j[0] is node and j[1] is weight
			if (distance[node] + j[1] < distance[j[0]]) and visited[j[0]] == False:
				distance[j[0]] = distance[node] + j[1]
				dis[j[0]] = distance[node] + j[1]
				parent[j[0]] = node
	print(distance)
	print(parent)


# main starts
g  = Graph()
g.addEdge('A', 'B', 5)
g.addEdge('A', 'E', 2)
g.addEdge('A', 'D', 9)
g.addEdge('B', 'C', 2)
g.addEdge('C', 'D', 3)
g.addEdge('D', 'F', 2)
g.addEdge('E', 'F', 3)
g.display_graph()
dijkstra(g, 'A')
