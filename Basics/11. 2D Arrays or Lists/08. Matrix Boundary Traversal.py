
# Problem statement

""" Given a matrix of integers containing ‘M’ rows and ‘N’ columns. Print the boundary elements of the matrix. The order of printing does not matter.

Note :
The output you will see will be in sorted order.
Your order of output does not matter.
You can return your result in any order. """


# solution


def matrixBoundaryTraversal(arr):
    # Iterate through each element of the matrix to find the boundary elements
    for i in range(len(arr)):  # Loop through rows
        for j in range(len(arr[0])):  # Loop through columns
            # Check if the current element is on the boundary (first or last row/column)
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[0]) - 1:
                yield arr[i][j]  # Return the boundary element using yield


# Input the number of rows and columns
rows = int(input())  # User input for the number of rows
cols = int(input())  # User input for the number of columns

# Input the 2D matrix, with each row being a list of integers
arr = [list(map(int, input().split())) for i in range(rows)]  # Reading the matrix row by row

# Print the boundary traversal result by converting the generator output to a list
print(list(matrixBoundaryTraversal(arr)))  # Convert the generator to a list and print it
