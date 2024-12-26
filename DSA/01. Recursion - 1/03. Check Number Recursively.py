# Problem statement

""" Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or
false.

Do this recursively. """


# solution


def checkNumber(arr, x, start, end):
    # Base case: single element
    if start == end:
        return arr[start] == x

    # Midpoint of the current range
    mid = (start + end) // 2

    # Divide and conquer: check in both halves
    return checkNumber(arr, x, start, mid) or checkNumber(arr, x, mid + 1, end)


# Input the size of the array and the array elements
n = int(input())
arr = list(map(int, input().split()))

# Input target value
x = int(input())

# Output the result
print(checkNumber(arr, x, 0, n - 1))
