
# Problem statement

""" You are given an integer array 'arr' of size 'N'.

You must sort this array using 'Bubble Sort'.

Note:
Change in the input array itself. You don't need to return or print the elements.

Example:
Input: ‘N’ = 7
'arr' = [2, 13, 4, 1, 3, 6, 28]

Output: [1 2 3 4 6 13 28]

Explanation: After applying bubble sort on the input array, the output is [1 2 3 4 6 13 28]. """


# solution


from typing import List


def swap(arr: List[int], index_1: int, index_2: int) -> None:
    """Swaps two elements in the array."""
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]


def bubbleSort(arr: List[int]) -> List[int]:
    # Get the length of the input array
    n = len(arr)

    # Outer loop: Iterate through each pass to sort the array
    for i in range(n - 1):
        swapped = False  # Flag to check if any swaps occurred in this pass

        # Inner loop: Compare each adjacent pair of elements in the array
        for j in range(n - 1 - i):  # Decrease the range as the largest elements get sorted
            if arr[j] > arr[j + 1]:  # If the current element is greater than the next element
                swap(arr, j, j + 1)  # Swap them to place the larger element at the right position
                swapped = True  # Set swapped to True to indicate a swap happened

        # If no swaps occurred, the array is already sorted, so we can break early
        if not swapped:
            break

    # Return the sorted array
    return arr


# Input Handling
n = int(input())
arr = [int(input()) for _ in range(n)]

# Sort and Output
print(bubbleSort(arr))

