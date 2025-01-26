
# Problem statement

""" Given a ‘N’ * ’M’ maze with obstacles, count and return the number of unique paths to reach the right-bottom cell from the top-left cell. A cell in the given maze has a value '-1' if it is a blockage or dead-end, else 0. From a given cell, we are allowed to move to cells (i+1, j) and (i, j+1) only. Since the answer can be large, print it modulo 10^9 + 7.

For Example :
Consider the maze below :
0 0 0
0 -1 0
0 0 0

There are two ways to reach the bottom left corner -

(1, 1) -> (1, 2) -> (1, 3) -> (2, 3) -> (3, 3)
(1, 1) -> (2, 1) -> (3, 1) -> (3, 2) -> (3, 3)

Hence the answer for the above test case is 2. """


# Solution


def uniquePaths(maze, n, m):
    # Initialize a 1D DP array with zeros
    dp = [0] * m

    # If the starting point is an obstacle, no paths are possible
    if maze[0][0] == -1:
        return 0

    # Set the starting point
    dp[0] = 1

    # Iterate through the grid row by row
    for i in range(n):
        for j in range(m):
            if maze[i][j] == -1:
                dp[j] = 0  # If the cell is an obstacle, no paths go through it
            elif j > 0:
                dp[j] += dp[j - 1]  # Update the current cell using the previous cell in the row

    # The last element in the DP array contains the number of unique paths
    return dp[-1]


# Input handling
n = int(input())
m = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(uniquePaths(maze, n, m))

