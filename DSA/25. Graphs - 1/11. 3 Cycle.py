
# Problem statement

""" Given a graph with N vertices (numbered from 0 to N-1) and M undirected edges, then count the
distinct 3-cycles in the graph. A 3-cycle PQR is a cycle in which (P,Q), (Q,R) and (R,P) are connected by an edge. """


# Solution


import sys


def count_3_cycles(graph, N):
    """
    Counts the number of 3-cycles (triangles) in an undirected graph.

    Parameters:
    graph (list of list): Adjacency matrix representation of the graph.
    N (int): Number of vertices.

    Returns:
    int: The number of 3-cycles in the graph.
    """
    count = 0

    # Iterate through all triplets of vertices
    for i in range(N):
        for j in range(i + 1, N):  # Avoid duplicate pairs
            if graph[i][j]:  # Edge exists
                for k in range(j + 1, N):
                    # Check if a cycle is formed
                    if graph[j][k] and graph[k][i]:
                        count += 1

    return count


# Input handling
n, m = map(int, input().split())

# Initialize adjacency matrix (n x n) with zeros
graph = [[0] * n for _ in range(n)]

# Read edges and construct adjacency matrix
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1  # Since the graph is undirected

# Output result
print(count_3_cycles(graph, n))
