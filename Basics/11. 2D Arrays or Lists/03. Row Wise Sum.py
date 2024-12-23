
# Problem statement

""" For a given two-dimensional integer array/list of size (N x M), find and print the sum of each of the row elements
in a single line, separated by a single space. """


# solution


def rowWiseSum(arr):
    # Iterate through each row of the 2D array
    for row in arr:
        # Calculate the sum of the current row and yield it
        yield sum(row)


# Input the number of rows and columns
rows = int(input())
cols = int(input())

# Input the 2D array row by row
arr = [list(map(int, input().split())) for i in range(rows)]

# Use the generator to calculate row-wise sums and print them
for row_sum in rowWiseSum(arr):
    print(row_sum, end=" ")
