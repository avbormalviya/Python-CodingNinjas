# Problem statement

""" You have been given an undirected graph with 'N' vertices and 'M' edges. The vertices are labelled from 1 to 'N'.
Your task is to find if the graph contains a cycle or not.
A path that starts from a given vertex and ends at the same vertex traversing the edges only once is called a cycle.

Note:

1. There are no parallel edges between two vertices.
2. There are no self-loops(an edge connecting the vertex to itself) in the graph.
3. The graph can be disconnected.

For Example :

Input: N = 3 , Edges =  [[1, 2], [2, 3], [1, 3]].
Output: Yes

Explanation : There are a total of 3 vertices in the graph. There is an edge between vertex 1 and 2,
vertex 2 and 3 and vertex 1 and 3. So, there exists a cycle in the graph. """


# Solution


def dfs(node, parent, visited, adj):
    visited[node] = True

    for neighbour in adj[node]:
        if not visited[neighbour]:
            if dfs(neighbour, node, visited, adj):
                return True  # Cycle found, propagate back
        elif neighbour != parent:
            return True  # Cycle detected

    return False  # No cycle in this path


def isCycle(V, adj):
    visited = [False] * V

    for i in range(V):  # Check all components (handles disconnected graphs)
        if not visited[i]:
            if dfs(i, -1, visited, adj):
                return True  # If any component has a cycle, return True

    return False  # No cycles found


# Input Handling
V, E = map(int, input().split())
adj = [[] for _ in range(V)]

for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # Because it'scratch_KNN.py an **undirected graph**

# Output
print("Yes" if isCycle(V, adj) else "No")
