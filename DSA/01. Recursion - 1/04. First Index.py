# Problem statement

""" Given an array of length N and an integer x, you need to find and return the first index of integer x present in the array. Return -1 if it is not present in the array.

First index means, the index of first occurrence of x in the input array.

Do this recursively. Indexing in the array starts from 0. """


# solution


def firstIndexHelper(arr, x, start):
    # Base case: If we've reached the end of the array
    if start == len(arr):
        return -1

    # If the current element matches x
    if arr[start] == x:
        return start

    # Recursive call for the next index
    return firstIndexHelper(arr, x, start + 1)


def firstIndex(arr, x):
    return firstIndexHelper(arr, x, 0)


# Input the size of the array and the array elements
n = int(input())
arr = list(map(int, input().split()))

# Input the target value
x = int(input())

# Output the result
result = firstIndex(arr, x)
print(result if result != -1 else "Element not found")
