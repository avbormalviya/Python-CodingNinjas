
# Problem statement

""" You are given an integer array 'arr' of size 'N'.

Note:
Change in the input array itself. You don't need to return or print the elements. """


# solution


def insertionSort(arr):
    # Loop through the array starting from the second element
    for curr in range(1, len(arr)):
        key = arr[curr]  # The element to be placed in the correct position
        i = curr - 1

        # Shift elements of the sorted portion to the right
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1

        # Place the key in its correct position
        arr[i + 1] = key

    return arr


# Input Handling
n = int(input())
arr = [int(input()) for _ in range(n)]

# Sort and Output
print(insertionSort(arr))
