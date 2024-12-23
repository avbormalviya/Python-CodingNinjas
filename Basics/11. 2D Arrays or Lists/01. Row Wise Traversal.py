
# Problem statement

""" Given a matrix, ‘A’ of size ‘N’ * ‘M’, you must traverse the matrix row-wise.

You must return an integer array of size ‘N’ * ‘M’ denoting the row-wise traversal of the matrix. """


# solution


def rowWiseTraversal(arr):
    # Flatten the 2D array row by row and return the result as a single list
    return [val for row in arr for val in row]


# Input the number of rows and columns for the 2D array
rows = int(input())
cols = int(input())

# Input the entire 2D array; each row is entered as a space-separated string of integers
# The input is converted into a list of lists using map and list comprehension
arr = [list(map(int, input().split())) for i in range(rows)]

# Perform row-wise traversal and print the flattened list
print(rowWiseTraversal(arr))
