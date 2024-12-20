# Problem statement

""" You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s. Write a solution to sort this
array/list in a 'single scan'.

'Single Scan' refers to iterating over the array/list just once or to put it in other words, you will be visiting each
element in the array/list just once.

Note:
1. You need to change in the given array/list itself. Hence, no need to return or print anything.
2. You are not allowed to sort the list/array directly.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
Time Limit: 1 sec """


# solution


def sortZeroOneTwo(arr):
    # Initialize pointers:
    # 'low' points to the position where the next 0 should go
    # 'mid' is the current element being evaluated
    # 'high' points to the position where the next 2 should go
    low = 0
    mid = 0
    high = len(arr) - 1

    # Loop until 'mid' crosses 'high'
    while mid <= high:
        if arr[mid] == 0:  # If the current element is 0
            # Swap the current element with the element at 'low'
            arr[low], arr[mid] = arr[mid], arr[low]
            # Move both 'low' and 'mid' pointers forward
            low += 1
            mid += 1

        elif arr[mid] == 1:  # If the current element is 1
            # No swap needed; just move the 'mid' pointer forward
            mid += 1

        else:  # If the current element is 2
            # Swap the current element with the element at 'high'
            arr[mid], arr[high] = arr[high], arr[mid]
            # Move the 'high' pointer backward
            high -= 1

    # Return the sorted array
    return arr


# Input Handling
n = int(input())
arr = [int(input()) for i in range(n)]

# Output the result
print(sortZeroOneTwo(arr))
