
# Problem statement

""" For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:

a. First row(left to right)
b. Last column(top to bottom)
c. Last row(right to left)
d. First column(bottom to top)

Mind that every element will be printed only once. """


# solution


def spiralTraversal(arr):
    top, bottom = 0, len(arr) - 1  # Row boundaries
    left, right = 0, len(arr[0]) - 1  # Column boundaries
    result = []

    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for i in range(left, right + 1):
            result.append(arr[top][i])
        top += 1

        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            result.append(arr[i][right])
        right -= 1

        # Traverse from right to left along the bottom row (if not already traversed)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(arr[bottom][i])
            bottom -= 1

        # Traverse from bottom to top along the left column (if not already traversed)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(arr[i][left])
            left += 1

    return result


# Input the number of rows and columns
rows = int(input())
cols = int(input())
#
# # Input the 2D matrix
arr = [list(map(int, input().split())) for i in range(rows)]

# Output the spiral traversal of the matrix
print(spiralTraversal(arr))
