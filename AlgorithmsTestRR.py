from graph.Graph import Graph
from algorithms.floyd_warshall import *
from algorithms.dijkstra import *
from algorithms.rr import *

sources = [1, 2, 3, 0, 2, 3]
targets = [0, 0, 0, 4, 1, 1]
weights = [3, 2, 4, 1, 3, 2]

graph = Graph(sources, targets, weights, False)
source = 1

dist_source = Dijkstra(source, graph)
print(dist_source)

dist = Floyd_Warshall(graph)
print(dist)

graph.vertex_update(source=1, target=0)

print("<--------Dijkstra_Truncated------->\n")

dist_source_rr = Dijkstra_Truncated(graph, dist_source)
print(dist_source_rr)

print("<--------Bfs_Truncated------->\n")

dist_rr = Bfs_Truncated(graph, source, dist)
print(dist_rr)

dist_rr_all = Bfs_Truncated_With_Sources(graph, dist)
print(dist_rr_all)

dist2 = Floyd_Warshall(graph)
print(dist2)

graph.draw()
