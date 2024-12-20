
# Problem statement

""" You have been given a random integer array/list(ARR) of size N. Write a function that rotates the given array/list
by D elements(towards the left).

Note:
Change in the input array/list itself.You don't need to return or print the elements.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= t <= 10^4
0 <= N <= 10^6
0 <= D <= N
Time Limit: 1 sec """


# solution


def rotateArray(arr, k):
    # Handle cases where k is larger than the array length
    k %= len(arr)
    # Rotate the array to the left
    return arr[k:] + arr[:k]


# Input Handling
n = int(input())
arr = [int(input()) for i in range(n)]

k = int(input())

# Output the result
print(rotateArray(arr, k))
