
# Problem statement

""" Given an array of integers, find the Kth largest sum subarray For example, given the array [1, -2, 3, -4, 5]
and K = 2, the 2nd largest sum subarray would be [3, -4, 5], which has a sum of 4.

Please note that a subarray is the sequence of consecutive elements of the array. """


# Solution


import heapq  # Importing heapq for min-heap operations


def kth_largest_sum_subarray(arr, k):
    """
    Finds the k-th largest sum of contiguous subarrays in an array.

    Parameters:
    arr (list): List of integers representing the array.
    k (int): The position (1-based) of the largest sum to find.

    Returns:
    int: The k-th largest sum among all subarrays.
    """
    heap = []  # Min-heap to keep track of the k largest sums

    # Iterate over all subarrays
    for i in range(len(arr)):
        current_sum = 0  # Initialize sum for subarray starting at index i

        for j in range(i, len(arr)):
            current_sum += arr[j]  # Add the current element to the subarray sum

            if len(heap) < k:
                # Add to heap if less than k elements are present
                heapq.heappush(heap, current_sum)
            elif current_sum > heap[0]:
                # Replace the smallest element if current_sum is larger
                heapq.heappop(heap)
                heapq.heappush(heap, current_sum)

    # The smallest element in the heap is the k-th largest sum
    return heap[0]


# Input: Size of the array
n = int(input())

# Input: Array elements
arr = list(map(int, input().split()))

# Input: Value of k
k = int(input())

# Output: Print the k-th largest sum of subarrays
print(kth_largest_sum_subarray(arr, k))
