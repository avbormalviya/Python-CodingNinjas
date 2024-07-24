# Problem statement

""" You have been given a random integer array/list(ARR) of size N, and an integer X. You need to search for the integer
X in the given array/list using 'Linear Search'.

 You have been required to return the index at which X is present in the array/list. If X has multiple occurrences in
the array/list, then you need to return the index at which the first occurrence of X would be encountered. In case X is
not present in the array/list, then return -1.

'Linear search' is a method for finding an element within an array/list. It sequentially checks each element of the
array/list until a match is found or the whole array/list has been searched. """

# solution

from sys import stdin


def linearSearch(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    else:
        return -1


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    val = int(stdin.readline().strip())
    print(linearSearch(arr, n, val))

    t -= 1
