
# Problem statement

""" You have been given a network of ‘N’ nodes from 1 to ‘N’ and ‘M’ edges. For each edge, you are given three values
(ui, vi, wi) where “ui” and “vi” denote the nodes and “wi” denotes an integer value which represents the time taken
by a signal to travel from “ui” to “vi”. Now, you are supposed to find the time which a signal takes to travel
from a given node ‘K’ to all nodes. If it is impossible for all nodes to receive the signal then print -1.

Note:
The signal which starts from the source node travels to all nodes simultaneously. """


# Solution


import heapq
import sys


def dijkstra(graph, N, start):
    """
    Dijkstra'scratch_KNN.py Algorithm to find shortest time from start node to all nodes.

    Parameters:
    graph (list of lists): Adjacency list where graph[i] contains (neighbor, weight).
    N (int): Number of nodes.
    start (int): Source node.

    Returns:
    int: Maximum time taken to reach any node, or -1 if some nodes are unreachable.
    """
    INF = sys.maxsize
    dist = [INF] * (N + 1)  # Distance array initialized to infinity
    dist[start] = 0  # Distance to start node is 0

    minHeap = [(0, start)]  # (time, node)

    while minHeap:
        curr_time, node = heapq.heappop(minHeap)  # Extract min distance node

        if curr_time > dist[node]:  # Ignore outdated distance values
            continue

        for neighbor, time in graph[node]:
            new_time = curr_time + time

            if new_time < dist[neighbor]:  # Relaxation step
                dist[neighbor] = new_time
                heapq.heappush(minHeap, (new_time, neighbor))

    # Find the maximum time among reachable nodes
    max_time = max(dist[1:])  # Ignore index 0 (1-based indexing)
    return max_time if max_time != INF else -1


# Input Handling
N, M, K = map(int, input().split())  # Nodes, Edges, Starting node
graph = [[] for _ in range(N + 1)]  # 1-based indexing

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # Since the graph is undirected

# Compute shortest time
result = dijkstra(graph, N, K)

# Output the result
print(result)
