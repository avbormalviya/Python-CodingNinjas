
# Problem statement

""" Given an undirected graph G(V,E), find and print all the connected components of the given graph G.

Note:

1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
2. E is the number of edges present in graph G.
3. You need to take input in main and create a function which should return all the connected components.

And then print them in the main, not inside function.
Print different components in new line. And each component should be printed in increasing order (separated by space).
Order of different components doesn't matter. """


# Solution


from collections import deque


class Graph:
    def __init__(self, vertices):
        """Initializes the graph with a given number of vertices."""
        self.V = vertices  # Number of vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list representation

    def addEdge(self, u, v):
        """Adds an undirected edge between vertices u and v."""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, node, visited, comp):
        """
        Performs Depth First Search (DFS) to find all nodes in a connected component.
        - node: Current node being explored
        - visited: List to track visited nodes
        - comp: Stores nodes in the current connected component
        """
        visited[node] = True  # Mark the node as visited
        comp.append(node)  # Add the node to the current component

        for neighbor in self.graph[node]:  # Explore all neighbors
            if not visited[neighbor]:  # If not visited, continue DFS
                self.DFS(neighbor, visited, comp)

    def findConnectedComponents(self):
        """
        Finds all connected components in the graph.
        Returns a list of lists, where each inner list represents a component.
        """
        visited = [False] * self.V  # Track visited nodes
        result = []  # Store all connected components

        for i in range(self.V):  # Iterate over all vertices
            if not visited[i]:  # If vertex is unvisited, start a new component
                comp = []
                self.DFS(i, visited, comp)
                result.append(sorted(comp))  # Store sorted component for consistent order

        return sorted(result)  # Sort components by their first element for cleaner output


# Input handling
V, E = map(int, input().split())  # Read number of vertices and edges

g = Graph(V)  # Create graph

# Read edges and add them to the graph
for _ in range(E):
    u, v = map(int, input().split())
    g.addEdge(u, v)

# Find and print connected components
for component in g.findConnectedComponents():
    print(*component)  # Print each component on a new line
