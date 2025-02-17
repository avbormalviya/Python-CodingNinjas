
# Problem statement

""" Given an undirected and disconnected graph G(V, E), print its BFS traversal.

Note:

1. Here you need to consider that you need to print BFS path starting from vertex 0 only.
2. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
3. E is the number of edges present in graph G.
4. Take graph input in the adjacency matrix.
5. Handle for Disconnected Graphs as well """


# Solution


def bfs_traversal(adj_matrix, V):
    visited = [False] * V
    queue = []

    for i in range(V):
        if not visited[i]:
            queue.append(i)
            visited[i] = True

            while queue:
                current_vertex = queue.pop(0)
                print(current_vertex, end=" ")

                for neighbor in range(V):
                    if adj_matrix[current_vertex][neighbor] == 1 and not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True

    return


V, E = map(int, input().split())
adj_matrix = [[0] * V for _ in range(V)]

for _ in range(E):
    u, v = map(int, input().split())
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1  # Since it's an undirected graph

bfs_traversal(adj_matrix, V)
