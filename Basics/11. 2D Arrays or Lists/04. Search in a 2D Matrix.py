
# Problem statement

""" You have been given a 2-D array 'MAT' of size M x N where 'M' and 'N' denote the number of rows and columns, respectively. The elements of each row are sorted in non-decreasing order.

Moreover, the first element of a row is greater than the last element of the previous row (if exists).

You are given an integer 'TARGET' and your task is to find if it exists in the given 'MAT' or not.

Example :

Given Matrix : 1 1 and Target : 8
               4 8

The output should be "TRUE" as 8 is present in the Matrix. """


# solution


def searchInA2DMatrix(arr, target):
    rows, cols = len(arr), len(arr[0])

    # Start binary search for the correct row
    row_low, row_high = 0, rows - 1

    while row_low <= row_high:
        row_mid = (row_high + row_low) // 2

        if arr[row_mid][0] <= target <= arr[row_mid][cols - 1]:
            # Binary search within the selected row
            col_low, col_high = 0, cols - 1
            while col_low <= col_high:
                col_mid = (col_high + col_low) // 2

                if arr[row_mid][col_mid] == target:
                    return row_mid, col_mid  # Found target

                elif arr[row_mid][col_mid] < target:
                    col_low = col_mid + 1
                else:
                    col_high = col_mid - 1

            return None  # Target not found in the row

        elif arr[row_mid][0] > target:
            row_high = row_mid - 1
        else:
            row_low = row_mid + 1

    return None  # Target not found in any row


# Input the number of rows and columns
rows = int(input())
cols = int(input())

# Input the 2D matrix
arr = [list(map(int, input().split())) for i in range(rows)]

# Input the target value
target = int(input())

# Perform the search and print the result
print(searchInA2DMatrix(arr, target))
