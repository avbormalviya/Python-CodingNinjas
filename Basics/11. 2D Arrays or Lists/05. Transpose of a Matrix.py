
# Problem statement

""" You are given a matrix ‘MAT’. Print and return the transpose of the matrix. The transpose of a matrix is obtained
by changing rows to columns and columns to rows. In other words, transpose of a matrix A[][] is obtained by changing
A[i][j] to A[j][i]. """


# solution


def transposeOfAMatrix(arr):
    rows, cols = len(arr), len(arr[0])
    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = arr[i][j]

    return transposed


# Input the number of rows and columns
rows = int(input())
cols = int(input())

# Input the 2D matrix
arr = [list(map(int, input().split())) for i in range(rows)]

# Print the transposed matrix
for row in transposeOfAMatrix(arr):
    print(' '.join(map(str, row)))
