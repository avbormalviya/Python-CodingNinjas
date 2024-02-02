# Problem statement

""" You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). Each number is present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3 and among these, there is a single integer value that is present twice. You need to find and return that duplicate number present in the array.

Note :
Duplicate number is always present in the given array/list. """

# solution


import sys


def duplicateNumber(arr, n):
    i = 0

    while i < n - 1:
        j = i + 1

        while j < n:
            if arr[i] == arr[j]:
                return arr[i]

            else:
                j += 1

        i += 1


# Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


# main
t = int(sys.stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1
