import heapq
from collections import defaultdict

def dijstra(graph, source):
    distance = [float('inf') for x in range(len(graph))]
    distance[source] = 0
    pq = [[0, source]]
    while len(pq) > 0:
        [d, node ] = heapq.heappop(pq)
        for [i, w] in graph[node]:
            if d + w < distance[i]:
                distance[i] = d + w 
                heapq.heappush(pq, [d + w, i])
    return distance
    

graph = defaultdict(list)

graph[0] = [[1, 1], [2, 2]]
graph[1] = [[0, 1],[3, 1], [4, 1]]
graph[2] = [[0, 2], [3, 3]]
graph[3] = [[2, 3], [4, 2]]
graph[4] = [[1, 1], [3, 2]]


print(dijstra(graph, 0))
