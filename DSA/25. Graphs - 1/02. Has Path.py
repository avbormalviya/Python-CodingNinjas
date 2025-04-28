
# Problem statement

"""Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), check if there exists any path between
them or not. Print true if the path exists and false otherwise.

Note:

1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
2. E is the number of edges present in graph G. """


# Solution


from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def addEdge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1  # Since it'scratch_KNN.py an undirected graph

    def hasPath(self, v1, v2):
        visited = [False] * self.V
        queue = deque([v1])
        visited[v1] = True

        while queue:
            node = queue.popleft()
            if node == v2:
                return True  # Path found

            for neighbor in range(self.V):
                if self.graph[node][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return False  # No path found


# Input handling
V, E = map(int, input().split())

g = Graph(V)

for _ in range(E):
    u, v = map(int, input().split())
    g.addEdge(u, v)

v1, v2 = map(int, input().split())

print(g.hasPath(v1, v2))
