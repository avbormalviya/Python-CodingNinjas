
# Problem statement

""" Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively. """


# solution


def sumOfArray(arr, start, end):
    # Base case: single element
    if start == end:
        return arr[start]
    # Base case: empty subarray
    if start > end:
        return 0

    # Midpoint of the current subarray
    mid = (start + end) // 2

    # Divide and conquer: sum left and right halves
    left_sum = sumOfArray(arr, start, mid)
    right_sum = sumOfArray(arr, mid + 1, end)

    return left_sum + right_sum


# Input the size of the array and the array elements
n = int(input())
arr = list(map(int, input().split()))

# Output the sum of the array
print(sumOfArray(arr, 0, n - 1))
