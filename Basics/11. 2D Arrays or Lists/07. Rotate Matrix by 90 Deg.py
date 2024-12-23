
# Problem statement

""" You are given a square matrix of non-negative integers 'MATRIX'. Your task is to rotate that array by 90 degrees in an
anti-clockwise direction using constant extra space. """


# solution


def rotateMatrixBy90Deg(arr):
    # Step 1: Reverse each row
    for row in arr:
        row.reverse()

    # Step 2: Transpose the matrix (swap rows with columns)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr[0])):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    return arr


# Input the number of rows and columns
rows = int(input())
cols = int(input())
#
# # Input the 2D matrix
arr = [list(map(int, input().split())) for i in range(rows)]

# Print the Result
print(rotateMatrixBy90Deg(arr))
