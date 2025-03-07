
# Problem statement

""" Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered
from 0 to V-1) and E number of edges.
Find and print the Minimum Spanning Tree (MST) using Kruskal's algorithm.

For printing MST follow the steps -
1. In one line, print an edge which is part of MST in the format -
v1 v2 w
where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1  <= v2 i.e.
print the smaller vertex first while printing an edge.
2. Print V-1 edges in above format in different lines.

Note : Order of different edges doesn't matter. """


# Solution


def kruskalMST(graph, V):
    """
    Kruskal's Algorithm to find the Minimum Spanning Tree (MST).

    Parameters:
    graph (list of lists): Each element is [u, v, w] representing an edge (u-v) with weight w.
    V (int): Number of vertices.

    Returns:
    list: The edges included in the MST.
    """
    # Sort edges by weight (ascending order)
    graph.sort(key=lambda x: x[2])

    # Union-Find structures
    parent = [i for i in range(V)]
    rank = [0] * V  # Rank array for union by rank

    def findParent(v):
        """Find the root of v with path compression."""
        if parent[v] != v:
            parent[v] = findParent(parent[v])  # Path compression
        return parent[v]

    def union(u, v):
        """Union by rank to keep tree balanced."""
        rootU = findParent(u)
        rootV = findParent(v)

        if rootU == rootV:
            return False  # Already connected, don't include in MST

        if rank[rootU] > rank[rootV]:
            parent[rootV] = rootU
        elif rank[rootU] < rank[rootV]:
            parent[rootU] = rootV
        else:
            parent[rootV] = rootU
            rank[rootU] += 1  # Increase rank when merging

        return True

    mst = []  # Store the MST edges

    # Process each edge
    for u, v, w in graph:
        if union(u, v):
            mst.append((u, v, w))

    return mst


# Input Handling
V, E = map(int, input().split())
graph = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph.append([u, v, w])

# Compute MST
mst_edges = kruskalMST(graph, V)

# Output MST edges
for u, v, w in mst_edges:
    print(u, v, w)
