# Problem statement

""" You have been given a random integer array/list(ARR) of size N. You are required to find and return
the second largest element present in the array/list. """

# solution

from sys import stdin


def secondLargestElement(arr, n):
    firstlargest = -2147483648
    secondLargest = -2147483648

    for i in arr:

        if firstlargest < i:
            secondLargest, firstlargest = firstlargest, i
        elif secondLargest < i:
            secondLargest = i
    else:
        return secondLargest


def takeInput():
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


# main
arr, n = takeInput()
print(secondLargestElement(arr, n))
