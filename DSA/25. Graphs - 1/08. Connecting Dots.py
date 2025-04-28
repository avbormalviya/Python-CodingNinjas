
# Problem statement

""" Gary has a board of size NxM. Each cell in the board is a coloured dot. There exist only 26 colours
denoted by uppercase Latin characters (i.e. A,B,...,Z). Now Gary is getting bored and wants to play a game.
The key of this game is to find a cycle that contain dots of same colour. Formally, we call a sequence of
dots d1, d2, ..., dk a cycle if and only if it meets the following condition:

1. These k dots are different: if i ≠ j then di is different from dj.
2. k is at least 4.
3. All dots belong to the same colour.
4. For all 1 ≤ i ≤ k - 1: di and di + 1 are adjacent. Also, dk and d1 should also be adjacent.
Cells x and y are called adjacent if they share an edge.

Since Gary is colour blind, he wants your help. Your task is to determine if there exists a cycle on the board. """


# Solution


move = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Directions: Down, Up, Right, Left


def dfs(arr, x, y, parent_x, parent_y, visited):
    visited[x][y] = True

    for dx, dy in move:
        new_x, new_y = x + dx, y + dy

        # Check boundaries
        if new_x < 0 or new_x >= len(arr) or new_y < 0 or new_y >= len(arr[0]):
            continue

        # Check if it'scratch_KNN.py the same character
        if arr[new_x][new_y] != arr[x][y]:
            continue

        # Cycle detected (excluding the parent node)
        if visited[new_x][new_y] and (new_x, new_y) != (parent_x, parent_y):
            return True

        # If not visited, explore deeper
        if not visited[new_x][new_y]:
            if dfs(arr, new_x, new_y, x, y, visited):
                return True

    return False


def hasCycle(arr):
    n, m = len(arr), len(arr[0])
    visited = [[False] * m for _ in range(n)]

    # Check every unvisited position in the grid
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:  # Start DFS from each unvisited node
                if dfs(arr, i, j, -1, -1, visited):
                    return True
    return False


# Input Handling
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

# Output Result
print(hasCycle(arr))
