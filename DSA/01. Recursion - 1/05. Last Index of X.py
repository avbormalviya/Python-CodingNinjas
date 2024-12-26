
# Problem statement

""" Given an array of length N and an integer x, you need to find and return the last index of integer x present in the
array. Return -1 if it is not present in the array.

Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.

You should start traversing your array from 0, not from (N - 1).

Do this recursively. Indexing in the array starts from 0. """


def lastIndexOfXHelper(arr, x, end):
    # Base case: If we've reached beyond the first index
    if end < 0:
        return -1

    # If the current element matches x
    if arr[end] == x:
        return end

    # Recursive call for the previous index
    return lastIndexOfXHelper(arr, x, end - 1)


def lastIndexOfX(arr, x):
    return lastIndexOfXHelper(arr, x, len(arr) - 1)


# Input the size of the array and the array elements
n = int(input())
arr = list(map(int, input().split()))

# Input the target value
x = int(input())

# Output the result
result = lastIndexOfX(arr, x)
print(result if result != -1 else "Element not found")
