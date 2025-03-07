
# Problem statement

""" An island is a small piece of land surrounded by water . A group of islands is said to be connected
if we can reach from any given island to any other island in the same group . Given V islands (numbered from 0 to V-1)
and E connections or edges between islands. Can you count the number of connected groups of islands. """


# Solution


def dfs(graph, node, visited):
    """
    Depth-First Search (DFS) to explore a connected component.

    Parameters:
    graph (list of lists): Adjacency list of the graph.
    node (int): Current node.
    visited (list of bool): Keeps track of visited nodes.
    """
    stack = [node]

    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = True
            stack.extend(graph[curr])  # Add all neighbors to stack


def count_islands(graph, V):
    """
    Counts the number of connected components (islands) in an undirected graph.

    Parameters:
    graph (list of lists): Adjacency list representation.
    V (int): Number of vertices.

    Returns:
    int: Number of connected components.
    """
    visited = [False] * V
    count = 0

    for i in range(V):
        if not visited[i]:  # New connected component
            dfs(graph, i, visited)
            count += 1

    return count


# Input Handling
V, E = map(int, input().split())
graph = [[] for _ in range(V)]  # 0-based indexing

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # Since the graph is undirected

# Compute and print number of islands
print(count_islands(graph, V))
