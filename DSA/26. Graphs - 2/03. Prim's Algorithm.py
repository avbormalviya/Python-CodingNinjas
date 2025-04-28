
# Problem statement

""" Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered
from 0 to V-1) and E number of edges.
Find and print the Minimum Spanning Tree (MST) using Prim'scratch_KNN.py algorithm.

For printing MST follow the steps -

1. In one line, print an edge which is part of MST in the format -
v1 v2 w
where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1  <= v2 i.e.
print the smaller vertex first while printing an edge.
2. Print V-1 edges in above format in different lines.
Note: Order of different edges doesn't matter. """


# Solution


import heapq

import heapq


def primMST(graph, V):
    """
    Prim'scratch_KNN.py Algorithm to find the Minimum Spanning Tree (MST).

    Parameters:
    graph (list of lists): Adjacency list where graph[i] contains (neighbor, weight).
    V (int): Number of vertices.

    Returns:
    list: The edges included in the MST.
    """
    if V == 0:
        return []

    visited = [False] * V
    minHeap = []
    result = []

    # Start Prim'scratch_KNN.py algorithm from node 0
    heapq.heappush(minHeap, (0, 0, -1))  # (weight, current_node, parent)

    while minHeap:
        wt, curr, parent = heapq.heappop(minHeap)

        if visited[curr]:  # Skip if already included in MST
            continue

        visited[curr] = True  # Mark node as visited

        if parent != -1:
            result.append((parent, curr, wt))

        # Push all adjacent unvisited edges to the heap
        for neighbor, weight in graph[curr]:
            if not visited[neighbor]:
                heapq.heappush(minHeap, (weight, neighbor, curr))

    return result


# Input Handling
V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # Use tuple (v, w)
    graph[v].append((u, w))  # Since graph is undirected

# Compute MST
mst_edges = primMST(graph, V)

# Output MST edges
for u, v, w in mst_edges:
    print(u, v, w)
