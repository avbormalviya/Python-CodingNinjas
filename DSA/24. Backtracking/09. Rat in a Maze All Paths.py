
# Problem statement

""" You are given a 'N' * 'N' maze with a rat placed at 'MAZE[0][0]'. Find and print all paths that rat can follow
to reach its destination i.e. 'MAZE['N' - 1]['N' - 1]'. Rat can move in any direc­tion ( left, right, up and down).

Value of every cell in the 'MAZE' can either be 0 or 1. Cells with value 0 are blocked means the rat
can­not enter into those cells and those with value 1 are open. """


# Solution


def searchMaze(maze, n, i, j, path, result):
    # Boundary conditions and obstacles check
    if i < 0 or i >= n or j < 0 or j >= n or maze[i][j] == 0:
        return

    # If we reach the destination, store the current path
    if i == n - 1 and j == n - 1:
        result.append(path.copy())
        return

    # Mark the cell as visited
    maze[i][j] = 0  # Temporarily block the path
    path[i * n + j] = 1  # Mark the path in the 1D array

    # Explore all four directions
    searchMaze(maze, n, i + 1, j, path, result)  # Down
    searchMaze(maze, n, i - 1, j, path, result)  # Up
    searchMaze(maze, n, i, j + 1, path, result)  # Right
    searchMaze(maze, n, i, j - 1, path, result)  # Left

    # Backtrack (undo changes)
    maze[i][j] = 1  # Unblock the path
    path[i * n + j] = 0  # Unmark the path


def findPaths(maze, n):
    result = []
    path = [0] * (n * n)  # 1D array representing the path

    if maze[0][0] == 1:
        searchMaze(maze, n, 0, 0, path, result)

    return result


# Input
n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]

# Solve and Print Paths
paths = findPaths(maze, n)
if paths:
    for path in paths:
        print(path)
else:
    print("No Path Found")
