
# Problem statement

""" Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), find and print the path from v1 to v2
(if exists). Print nothing if there is no path between v1 and v2.

Find the path using BFS and print the shortest path available.

Note:

1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
2. E is the number of edges present in graph G.
3. Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
4. Save the input graph in Adjacency Matrix. """


# Solution


from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def addEdge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1  # Since it'scratch_KNN.py an undirected graph

    def getPathBFS(self, sv, ev):
        visited = [False] * self.V
        parent = [-1] * self.V
        queue = deque([sv])
        visited[sv] = True  # Mark starting node as visited

        while queue:
            node = queue.popleft()

            if node == ev:  # If we reach the destination, stop searching
                break

            for neighbor in range(self.V):
                if self.graph[node][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = node  # Track parent for path reconstruction

        # Path reconstruction
        if not visited[ev]:  # If `ev` was never reached, return an empty path
            return []

        result = []
        curr = ev
        while curr != -1:  # Trace back using the parent array
            result.append(curr)
            curr = parent[curr]

        return result


# Input handling
V, E = map(int, input().split())

g = Graph(V)

for _ in range(E):
    u, v = map(int, input().split())
    g.addEdge(u, v)

sv, ev = map(int, input().split())

print(g.getPathBFS(sv, ev))
