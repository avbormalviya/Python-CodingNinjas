
# Problem statement

""" Sort the given unsorted array 'arr' of size 'N' in non-decreasing order using the selection sort algorithm.

Note:
Change in the input array/list itself.

Example:

Input:
N = 5
arr = {8, 6, 2, 5, 1}

Output:
1 2 5 6 8 """


# solution


from typing import List


def findLowest(arr: List[int], start: int) -> int:
    """Finds the index of the smallest element in the array starting from 'start'."""
    low = float('inf')
    index = start

    for i in range(start, len(arr)):
        if arr[i] < low:
            low = arr[i]
            index = i

    return index


def swap(arr: List[int], index_1: int, index_2: int) -> None:
    """Swaps two elements in the array."""
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]


def selectionSort(arr: List[int]) -> List[int]:
    """Sorts the array in-place using Selection Sort."""
    for curr in range(len(arr) - 1):
        min_index = findLowest(arr, curr)  # Get the index of the smallest element
        swap(arr, curr, min_index)        # Swap it with the current element

    return arr


# Input Handling
n = int(input())
arr = [int(input()) for _ in range(n)]

# Sort and Output
print(selectionSort(arr))

