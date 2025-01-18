
# Problem statement

""" Given an integer array of size N. Sort this array (in decreasing order) using heap sort.

Note: Space complexity should be O(1). """


# Solution


def heapify(arr, n, i):
    """
    Ensures the subtree rooted at index i satisfies the max-heap property.
    :param arr: List[int] - The array representation of the heap
    :param n: int - The size of the heap
    :param i: int - The current index in the heap
    """
    lowest = i  # Assume the current node is the largest
    leftChildIndex = 2 * i + 1  # Left child
    rightChildIndex = 2 * i + 2  # Right child

    # Check if the left child exists and is larger than the current largest
    if leftChildIndex < n and arr[leftChildIndex] < arr[lowest]:
        lowest = leftChildIndex

    # Check if the right child exists and is larger than the current largest
    if rightChildIndex < n and arr[rightChildIndex] < arr[lowest]:
        lowest = rightChildIndex

    # If the largest element is not the current node, swap and heapify the affected subtree
    if lowest != i:
        arr[i], arr[lowest] = arr[lowest], arr[i]
        heapify(arr, n, lowest)


def heapSort(arr):
    """
    Sorts an array using the heap sort algorithm.
    :param arr: List[int] - The array to be sorted
    :return: List[int] - The sorted array
    """
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move the current root (largest element) to the end
        arr[0], arr[i] = arr[i], arr[0]
        # Call heapify on the reduced heap
        heapify(arr, i, 0)

    return arr


# Input and output
n = int(input())  # Number of elements in the array
arr = [int(x) for x in input().split()]  # The array of integers
heapSort(arr)
print(*arr)  # Print the sorted array
