
# Problem statement

""" You have been given an N*M matrix filled with integer numbers, find the maximum sum that can be obtained
from a path starting from any cell in the first row to any cell in the last row.

From a cell in a row, you can move to another cell directly below that row, or diagonally below left or right.
So from a particular cell (row, col), we can move in three directions i.e.

Down: (row+1,col)
Down left diagonal: (row+1,col-1)
Down right diagonal: (row+1, col+1) """


# Solution


def maximumPathSum(matrix, n, m):
    # Process the matrix starting from the second-to-last row and move upwards
    for i in range(n - 2, -1, -1):  # Iterate through rows from bottom to top
        for j in range(m):  # Iterate through each column in the current row
            # For each cell in row 'i', update its value by adding the maximum of the three cells below it
            # max(j - 1, 0) ensures we don't access out-of-bounds columns (left diagonal)
            # min(j + 2, m) ensures we don't access out-of-bounds columns (right diagonal)
            matrix[i][j] += max(matrix[i + 1][max(j - 1, 0):min(j + 2, m)])

    # After processing all rows, the top row will contain the maximum path sum in the first column
    return max(matrix[0])


# Input the number of rows and columns in the matrix
n = int(input())  # Number of rows in the matrix
m = int(input())  # Number of columns in the matrix

# Input the matrix, which consists of 'n' rows and 'm' columns
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output the maximum path sum starting from any cell in the top row
print(maximumPathSum(matrix, n, m))
