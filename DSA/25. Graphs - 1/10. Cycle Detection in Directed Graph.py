
# Problem statement

""" Given a directed graph, check whether the graph contains a cycle or not. Your function should return true
if the given graph contains at least one cycle, else return false. """


# Solution


def dfs(node, visited, rec_stack, adj):
    visited[node] = True
    rec_stack[node] = True  # Mark node as part of recursion stack

    for neighbour in adj[node]:
        if not visited[neighbour]:
            if dfs(neighbour, visited, rec_stack, adj):
                return True  # Cycle detected
        elif rec_stack[neighbour]:
            return True  # Back edge found, cycle detected

    rec_stack[node] = False  # Remove from recursion stack
    return False


def isCycle(V, adj):
    visited = [False] * V
    rec_stack = [False] * V  # Keeps track of recursion stack

    for i in range(V):  # Check for cycles in all components
        if not visited[i]:
            if dfs(i, visited, rec_stack, adj):
                return True

    return False


# Input Handling
V, E = map(int, input().split())
adj = [[] for _ in range(V)]

for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)  # Directed graph, add only u -> v

# Output
print("Yes" if isCycle(V, adj) else "No")
