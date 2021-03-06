import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.forest import *
from algorithms.floyd_warshall import *

graph = Graph.creategraph_for_worst_escenary_edge_insert(30)
result_before_dist = np.array(Floyd_Warshall(graph))

graph.dynamic_incremental_edge_middle()

result_after_dist = np.array(Floyd_Warshall(graph))

def test_forest_worst():
    dist_forest = Forest_apsp(graph, result_before_dist)
    np.testing.assert_array_equal(dist_forest, result_after_dist)
