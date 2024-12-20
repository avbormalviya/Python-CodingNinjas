
# Problem statement

""" You have been given an integer array/list(ARR) of size N. It has been sorted(in increasing order) and then rotated
by some number 'K' (K is greater than 0) in the right hand direction.

Your task is to write a function that returns the value of 'K', that means, the index from which the array/list has
been rotated.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= t <= 10^2
2 <= N <= 10^5
Time Limit: 1 sec """


# solution


def checkArrayRotation(arr):
    if len(arr) <= 1:
        return 0

    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return i

    return 0


# Input Handling
n = int(input())  # Read the size of the array
arr = [int(input()) for i in range(n)]  # Read the elements of the array

# Output the result
print(checkArrayRotation(arr))
