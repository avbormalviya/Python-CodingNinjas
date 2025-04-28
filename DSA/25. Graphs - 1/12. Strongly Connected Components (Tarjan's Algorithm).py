
# Problem statement

""" You are given an unweighted directed graph of 'V' vertices and 'E' edges. Your task is to print all the
strongly connected components (SCCs) present in the graph. """


# Solution


def dfs(node, visited, discovered, low, stack, isInStack, time, adj, sccs):
    """
    Depth-First Search (DFS) function to find Strongly Connected Components (SCCs) using Tarjan’scratch_KNN.py Algorithm.
    """
    visited[node] = True
    discovered[node] = low[node] = time[0]  # Set discovery and low-link value
    time[0] += 1  # Increment global discovery time counter
    stack.append(node)  # Push the node onto the stack
    isInStack[node] = True  # Mark the node as being in the stack

    # Explore all adjacent nodes
    for neighbour in adj[node]:
        if not visited[neighbour]:  # If the node is not visited, recurse
            dfs(neighbour, visited, discovered, low, stack, isInStack, time, adj, sccs)
            low[node] = min(low[node], low[neighbour])  # Update low-link value
        elif isInStack[neighbour]:  # If neighbor is in stack, it'scratch_KNN.py a back edge
            low[node] = min(low[node], discovered[neighbour])

    # If the node is the head (root) of an SCC
    if low[node] == discovered[node]:
        component = []
        while stack:
            v = stack.pop()  # Remove the node from the stack
            isInStack[v] = False  # Mark it as out of the stack
            component.append(v)
            if v == node:  # Stop when SCC is fully formed
                break
        sccs.append(component)  # Store the SCC


def stronglyConnectedComponents(V, adj):
    """
    Finds all SCCs in a directed graph using Tarjan’scratch_KNN.py Algorithm.
    :param V: Number of vertices
    :param adj: Adjacency list of the graph
    :return: List of SCCs
    """
    visited = [False] * V  # Tracks visited nodes
    discovered = [-1] * V  # Stores discovery time of each node
    low = [-1] * V  # Stores the lowest discovery time reachable
    stack = []  # Stack for DFS traversal
    isInStack = [False] * V  # Checks if a node is in the stack
    time = [0]  # Time counter (list to allow modification in recursion)
    sccs = []  # List to store SCCs

    # Run DFS for every unvisited node
    for i in range(V):
        if not visited[i]:
            dfs(i, visited, discovered, low, stack, isInStack, time, adj, sccs)

    return sccs


# Input Handling
V, E = map(int, input().split())  # Read number of vertices and edges
adj = [[] for _ in range(V)]  # Initialize adjacency list

# Read edges
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)  # Directed edge from u to v

# Compute SCCs
sccs = stronglyConnectedComponents(V, adj)
print(sccs)
