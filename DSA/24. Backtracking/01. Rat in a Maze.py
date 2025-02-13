# Problem statement

""" You are given a starting position for a rat which is stuck in a maze at an initial point (0, 0) (the maze can be thought of as a 2-dimensional plane). The maze would be given in the form of a square matrix of order 'N' * 'N' where the cells with value 0 represent the maze’s blocked locations while value 1 is the open/available path that the rat can take to reach its destination. The rat's destination is at ('N' - 1, 'N' - 1). Your task is to find all the possible paths that the rat can take to reach from source to destination in the maze. The possible directions that it can take to move in the maze are 'U'(up) i.e. (x, y - 1) , 'D'(down) i.e. (x, y + 1) , 'L' (left) i.e. (x - 1, y), 'R' (right) i.e. (x + 1, y).

Note:
Here, sorted paths mean that the expected output should be in alphabetical order.

For Example:
Given a square matrix of size 4*4 (i.e. here 'N' = 4):
1 0 0 0
1 1 0 0
1 1 0 0
0 1 1 1

Expected Output:
DDRDRR DRDDRR
i.e. Path-1: DDRDRR and Path-2: DRDDRR

The rat can reach the destination at (3, 3) from (0, 0) by two paths, i.e. DRDDRR and DDRDRR when printed
in sorted order, we get DDRDRR DRDDRR. """


# Solution


def searchMaze(arr, n, i, j, path="", result=None):
    if result is None:
        result = []

    # Base case: If reached destination, store path and return
    if i == n - 1 and j == n - 1:
        result.append(path)
        return

    # Check boundary and obstacle conditions
    if i < 0 or j < 0 or i >= n or j >= n or arr[i][j] == 0:
        return

    # Mark current cell as visited
    arr[i][j] = 0

    # Explore all 4 directions
    searchMaze(arr, n, i - 1, j, path + "U", result)  # Up
    searchMaze(arr, n, i + 1, j, path + "D", result)  # Down
    searchMaze(arr, n, i, j + 1, path + "R", result)  # Right
    searchMaze(arr, n, i, j - 1, path + "L", result)  # Left

    # Backtrack: Unmark cell to explore other paths
    arr[i][j] = 1

    return result


# Input and execution
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Find paths from (0,0) to (n-1,n-1)
paths = searchMaze(arr, n, 0, 0)

# Print results
print(*paths, sep="\n")
