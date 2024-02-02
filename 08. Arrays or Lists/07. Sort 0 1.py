# Problem statement

""" You have been given an integer array/list(ARR) of size N that contains only integers, 0 and 1. Write a function to
sort this array/list. Think of a solution which scans the array/list only once and don't require use of an extra array/list.

Note:
You need to change in the given array/list itself. Hence, no need to return or print anything.  """

# solution


from sys import stdin


def sortZeroesAndOne(arr, n):
    i = 0
    j = n - 1

    while i < j:
        if arr[i] == 1 and arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j -= 1

        elif arr[i] == 0 and arr[j] == 0:
            i += 1

        elif arr[i] == 1 and arr[j] == 1:
            j -= 1

        elif arr[i] == 0 and arr[j] == 1:
            i += 1
            j -= 1


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1
