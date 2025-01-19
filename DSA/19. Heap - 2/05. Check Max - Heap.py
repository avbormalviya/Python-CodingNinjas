
# Problem statement

""" Given an array of integers, check whether it represents max-heap or not. Return true if the given array
represents max-heap, else return false. """


# Solution


def checkMaxHeap(arr, n):
    """
    Checks if the given array represents a max-heap.

    Parameters:
    arr (list): Array of integers representing the heap.
    n (int): Size of the array.

    Returns:
    bool: True if the array represents a max-heap, False otherwise.
    """
    # Iterate over all internal nodes (nodes with at least one child)
    for i in range(n // 2):
        # Check if the left child exists and is greater than the parent
        if 2 * i + 1 < n and arr[i] < arr[2 * i + 1]:
            return False

        # Check if the right child exists and is greater than the parent
        if 2 * i + 2 < n and arr[i] < arr[2 * i + 2]:
            return False

    # If all conditions are satisfied, it's a max-heap
    return True


# Input: Size of the array
n = int(input())

# Input: Array elements
arr = [int(i) for i in input().split()]

# Output: Check if the array represents a max-heap
print(checkMaxHeap(arr, n))
