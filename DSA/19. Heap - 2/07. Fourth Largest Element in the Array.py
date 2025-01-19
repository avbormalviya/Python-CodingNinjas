
# Problem statement

""" You are given an array consisting of 'N' integers. You have to find the fourth largest element present in the array.

If there is no such number present in the array, then print the minimum value of an integer which is -2147483648.

Follow Up:
Try solving this problem in O(N) time complexity. """


# Solution


from heapq import heappush, heappop  # Importing heapq for heap operations

def kthLargest(arr, k):
    """
    Finds the k-th largest element in the array using a min-heap.

    Parameters:
    arr (list): List of integers.
    k (int): The position (1-based) of the largest element to find.

    Returns:
    int: The k-th largest element in the array.
    """
    heap = []  # Initialize an empty min-heap

    # Step 1: Build a min-heap with the first k elements
    for i in range(k):
        heappush(heap, arr[i])  # Add elements to the heap

    # Step 2: Process the remaining elements in the array
    for i in range(k, len(arr)):
        # If the current element is greater than the smallest in the heap
        if arr[i] > heap[0]:
            heappop(heap)  # Remove the smallest element
            heappush(heap, arr[i])  # Add the current element

    # Step 3: Return the smallest element in the heap (k-th largest in the array)
    return heap[0]


# Input: Size of the array
n = int(input())

# Input: Array elements
arr = [int(i) for i in input().split()]

# Output: Print the k-th largest element in the array
print(kthLargest(arr, 4))
