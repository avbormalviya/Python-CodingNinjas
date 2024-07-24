# Problem statement

""" You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].

Now, in the given array/list, 'M' numbers are present twice and one number is present only once.

You need to find and return that number which is unique in the array/list.

Note:
Unique element is always present in the array/list according to the given condition. """

# solution

import sys


def findUnique(arr, n):
    i = 0
    j = 1

    while j < n:
        if arr[i] != arr[j]:
            j += 1

        else:
            arr.remove(arr[i])
            j -= 1
            arr.remove(arr[j])
            j = i + 1
            n -= 2

    return arr[i]


# Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


# main
t = int(sys.stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1
