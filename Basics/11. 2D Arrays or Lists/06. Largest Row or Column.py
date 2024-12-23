# Problem statement

""" You are given a 2D list (array) with dimensions N rows and M columns, filled with integers. Your task is to find
the row or column that has the largest sum of its elements.

Important Rules:
- If two or more rows/columns have the same sum, choose the one that comes first.
- If a row and a column have the same largest sum, choose the row.

Goal: Return which row or column has the largest sum. """

# solution


import numpy as np


def largestRowOrColumn(arr):
    # Compute row sums and column sums
    row_sums = arr.sum(axis=1)  # Sum along rows
    col_sums = arr.sum(axis=0)  # Sum along columns

    # Find the maximum row sum and its index
    max_row_sum = row_sums.max()
    max_row_index = row_sums.argmax()

    # Find the maximum column sum and its index
    max_col_sum = col_sums.max()
    max_col_index = col_sums.argmax()

    # Compare and return the result with the corresponding index
    if max_col_sum > max_row_sum:
        return f"Column {max_col_index}", max_col_sum
    else:
        return f"Row {max_row_index}", max_row_sum


# Input the number of rows and columns
rows = int(input())
cols = int(input())

# Input the 2D matrix
arr = [list(map(int, input().split())) for i in range(rows)]

# Print the Result
print(largestRowOrColumn(np.array(arr)))
