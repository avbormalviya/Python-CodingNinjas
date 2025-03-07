
# Problem statement

""" You are given an undirected graph with N nodes in the form of an adjacency matrix. You are also given an integer M.

Your task is to find if you can color the vertices of the graph using at most M colors such that no
two adjacent vertices are of the same color.

For example:

If the given adjacency matrix is:
[0 1 0]
[1 0 1]
[0 1 0] and M = 3.

The given adjacency matrix tells us that node 1 is connected to node 2 and node 2 is connected to node 3.

So if we color vertex 1 with ‘red’, vertex 2 with ‘blue’, and vertex 3 with ‘red’, it is possible
to color the given graph with two colors which is less than or equal to M. """


# Solution


def dfs(graph, visited, color, node, m, n):
    """
    Depth-First Search (DFS) for graph coloring.

    Parameters:
    graph (list of lists): Adjacency matrix representation of the graph.
    visited (list): Tracks visited nodes.
    color (list): Stores colors assigned to each node.
    node (int): Current node being colored.
    m (int): Number of colors available.
    n (int): Number of nodes.

    Returns:
    bool: True if coloring is possible, False otherwise.
    """
    visited[node] = True

    for neighbor in range(n):
        if graph[node][neighbor]:  # If there's an edge
            if color[neighbor] == color[node]:  # Conflict check
                return False
            if not visited[neighbor]:  # If not visited, color it
                color[neighbor] = (color[node] + 1) % m
                if not dfs(graph, visited, color, neighbor, m, n):
                    return False

    return True


def graphColoring(graph, n, m):
    """
    Checks if the given graph can be colored with at most m colors.

    Parameters:
    graph (list of lists): Adjacency matrix representation of the graph.
    n (int): Number of nodes.
    m (int): Number of colors available.

    Returns:
    bool: True if a valid m-coloring exists, False otherwise.
    """
    visited = [False] * n
    color = [-1] * n  # -1 means uncolored

    for node in range(n):
        if not visited[node]:  # Start DFS for unvisited components
            color[node] = 0  # Start with first color
            if not dfs(graph, visited, color, node, m, n):
                return False

    return True


# Input Handling (Adjacency Matrix)
n, m = map(int, input().split())  # Read number of vertices and colors
graph = [[0] * n for _ in range(n)]  # Initialize adjacency matrix

# Read edges
e = int(input())  # Number of edges
for _ in range(e):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1  # Undirected graph

# Compute and print result
print(graphColoring(graph, n, m))
