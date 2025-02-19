
# Problem statement

""" Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2
(if exists). Print nothing if there is no path between v1 and v2.

Find the path using DFS and print the first path that you encountered.

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
        self.graph[v][u] = 1  # Since it's an undirected graph

    def getPathDFSHelper(self, sv, ev, visited, parent):
        visited[sv] = True
        if sv == ev:
            return True  # Found the end vertex

        for neighbor in range(self.V):
            if self.graph[sv][neighbor] == 1 and not visited[neighbor]:
                parent[neighbor] = sv  # Track parent before recursive call
                if self.getPathDFSHelper(neighbor, ev, visited, parent):
                    return True

        return False

    def getPathDFS(self, sv, ev):
        visited = [False] * self.V
        parent = [-1] * self.V  # Use -1 to indicate no parent

        if not self.getPathDFSHelper(sv, ev, visited, parent):
            return []  # No path found

        result = [ev]
        while ev != sv:  # Traverse back to the source
            ev = parent[ev]
            result.append(ev)

        return result


# Input handling
V, E = map(int, input().split())

g = Graph(V)

for _ in range(E):
    u, v = map(int, input().split())
    g.addEdge(u, v)

sv, ev = map(int, input().split())

print(g.getPathDFS(sv, ev))
