# Problem statement

""" Given the 'start' and the 'end'' positions of the array 'input'. Your task is to sort the elements between 'start'
and 'end' using quick sort.

Note :
Make changes in the input array itself. """


# solution


def partitionArray(arr, start, end):
    pivot = arr[end]  # Choose pivot (here, the last element)
    i = start - 1  # Pointer to the smaller element

    # Rearrange elements to place pivot at correct position
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap smaller element with arr[i]

    # Swap the pivot element with the element at i + 1
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1  # Return the index of the pivot


def quickSort(arr, start, end):
    if start < end:
        # Partition the array and get the pivot index
        pivot_index = partitionArray(arr, start, end)

        # Recursively apply QuickSort to the left and right of the pivot
        quickSort(arr, start, pivot_index - 1)
        quickSort(arr, pivot_index + 1, end)


# Input: Read array size and elements
n = int(input())
arr = list(map(int, input().split()))

quickSort(arr, 0, n - 1)

print(arr)
