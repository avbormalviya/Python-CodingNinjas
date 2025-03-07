# Problem statement

# Given a DAG(direct acyclic graph), return the Topological Sorting of a given graph.


# Solution


from collections import deque


def _dfs_helper(adj, visited, stack, v):
    """
    Recursive DFS function to perform topological sorting.

    Parameters:
    adj (list): Adjacency list representation of the graph.
    visited (list): Tracks visited nodes.
    stack (deque): Stores the topological order.
    v (int): Current vertex.

    Returns:
    None
    """
    visited[v] = True  # Mark the current node as visited

    # Visit all unvisited neighbors
    for neighbor in adj[v]:
        if not visited[neighbor]:
            _dfs_helper(adj, visited, stack, neighbor)

    stack.appendleft(v)  # Append to the left for efficient topological order


def topological_sort(v, adj):
    """
    Performs topological sorting on a directed acyclic graph (DAG) using DFS.

    Parameters:
    v (int): Number of vertices.
    adj (list of lists): Adjacency list representation of the graph.

    Returns:
    list: Topological order of vertices.
    """
    visited = [False] * v  # Track visited nodes
    stack = deque()  # Use deque for efficient appending

    # Perform DFS from each unvisited node
    for i in range(v):
        if not visited[i]:
            _dfs_helper(adj, visited, stack, i)

    return list(stack)  # Convert deque to list for final output


# Input Handling
V, E = map(int, input().split())  # Read number of vertices and edges
adj = [[] for _ in range(V)]  # Initialize adjacency list

# Read edges
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)  # Directed edge from u to v

# Compute Topological Sorting
topological_order = topological_sort(V, adj)
print(topological_order)  # Print the topological order directly
