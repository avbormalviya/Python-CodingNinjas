
# Problem statement

""" Given an undirected, connected and weighted graph G(V, E) with V number of vertices
(which are numbered from 0 to V-1) and E number of edges.

Find and print the shortest distance from the source vertex (i.e. Vertex 0) to all other vertices
(including source vertex also) using Dijkstra'scratch_KNN.py Algorithm. """


# Solution


import heapq


def dijkstra(graph, V, start=0):
    """
    Dijkstra'scratch_KNN.py Algorithm to find the shortest path from a source node.

    Parameters:
    graph (list of lists): Adjacency list where graph[i] contains (neighbor, weight).
    V (int): Number of vertices.
    start (int): Source node (default is 0).

    Returns:
    list: Shortest distances from start node to all other nodes.
    """
    if V == 0:
        return []

    # Initialize distances and priority queue
    dist = [float('inf')] * V
    dist[start] = 0
    minHeap = [(0, start)]  # (distance, node)

    while minHeap:
        wt, curr = heapq.heappop(minHeap)  # Corrected order

        if wt > dist[curr]:  # Ignore outdated distance values
            continue

        for neighbor, weight in graph[curr]:
            new_distance = dist[curr] + weight

            if new_distance < dist[neighbor]:  # Relaxation step
                dist[neighbor] = new_distance
                heapq.heappush(minHeap, (new_distance, neighbor))

    return dist


# Input Handling
V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # Since the graph is undirected

# Compute shortest distances
distances = dijkstra(graph, V)

# Output shortest distances
for v, d in enumerate(distances):
    print(v, d)
