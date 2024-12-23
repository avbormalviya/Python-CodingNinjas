
# Problem statement

""" Given a matrix, ‘A’ of size ‘N’ * ‘M’, you must traverse the matrix column-wise.

You must return an integer array of size ‘N’ * ‘M’ denoting the column-wise traversal of the matrix. """


# solution


def columnWiseTraversal(arr):
    # Outer loop for columns (iterates column by column)
    for i in range(len(arr[0])):
        # Inner loop for rows (fetches values row by row for the current column)
        for j in range(len(arr)):
            yield arr[j][i]  # Yield element from the current column


# Input the number of rows and columns for the 2D array
rows = int(input())
cols = int(input())

# Input the 2D array row by row
arr = [list(map(int, input().split())) for i in range(rows)]

# Use the generator to perform column-wise traversal
print(list(columnWiseTraversal(arr)))
