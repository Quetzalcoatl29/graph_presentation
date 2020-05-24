from graph.Graph import Graph
from algorithms.floyd_warshall import *
from algorithms.dijkstra import *
from algorithms.knnb import *
from algorithms.rr import *
from algorithms.eg import *
from algorithms.quinca import *
from algorithms.abm import *
from algorithms.forest import *

from time import time
import statistics

class Algorithm():

    def __init__(self, values):
        self.attempt = 30
        self.graph = Graph.import_values(values)


    def list(self):
        return {
            'static': ['dijkstra-apsp', 'floyd-warshall'],
            'incremental': [
                'rr-bfs-truncated',
                'even-gazit',
                'quinca',
                'abm',
                'forest'
            ]
        }

    def run_algorithm(self, algorithm, dist=[[]]):

        if algorithm == 'dijkstra-apsp':
            return self.run_algorithm_dijkstra_apsp()

        if algorithm == 'floyd-warshall':
            return self.run_algorithm_floyd_warshall()

        if algorithm == 'rr-bfs-truncated':
            return self.run_algorithm_rr_bfs_truncated(dist.copy())

        if algorithm == 'even-gazit':
            return self.run_algorithm_eg(dist.copy())

        if algorithm == 'quinca':
            return self.run_algorithm_quinca(dist.copy())

        if algorithm == 'abm':
            return self.run_algorithm_abm(dist.copy())

        if algorithm == 'forest':
            return self.run_algorithm_forest(dist.copy())

    def run_algorithm_floyd_warshall(self):
        t = time()
        dist = Floyd_Warshall(self.graph)
        time_seconds = time() - t

        return self.export_algorithm(dist, time_seconds)

    def run_algorithm_dijkstra(self, source):
        t = time()
        dist = Dijkstra(int(source), self.graph)
        time_seconds = time() - t

        return self.export_algorithm([dist], time_seconds)

    def run_algorithm_dijkstra_apsp(self):
        times = []
        for tried in range(self.attempt):
            t = time()
            dist = Dijkstra_apsp(self.graph)
            time_seconds = time() - t
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_rr_bfs_truncated(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            dist = Bfs_Truncated_With_Sources(self.graph, dist)
            time_seconds = time() - t
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_knnb_node_incremental(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            dist = KNNB_Node_Incremental(self.graph, dist)
            time_seconds = time() - t
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_eg(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            dist = Even_Gazit(self.graph, dist)
            time_seconds = time() - t
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_quinca(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            dist = Quinca(self.graph, dist)
            time_seconds = time() - t
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_abm(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            dist = ABM_Update(self.graph, dist)
            time_seconds = time() - t
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_forest(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            dist = Forest_apsp(self.graph, dist)
            time_seconds = time() - t
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def export_algorithm(self, dist, times):
        return {
            'matrix': dist,
            'mean_times': statistics.mean(times) * 1000,
            'stdev_times': statistics.stdev(times),
        }
