# Problem statement

""" You have been given an empty array(ARR) and its size N. The only input taken from the user will be N and you need
not worry about the array.

Your task is to populate the array using the integer values in the range 1 to N(both inclusive) in the order -
1,3,5,.......,6,4,2.

Note:
You need not print the array. You only need to populate it. """

# solution


from sys import stdin


def arrange(arr, n):
    i = 0
    j = n - 1

    for count in range(n):
        if count % 2 == 0:
            count += 1
            arr[i] = count
            i += 1

        else:
            count += 1
            arr[j] = count
            j -= 1


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    n = int(stdin.readline().strip())
    arr = n * [0]
    arrange(arr, n)
    printList(arr, n)
    t -= 1
