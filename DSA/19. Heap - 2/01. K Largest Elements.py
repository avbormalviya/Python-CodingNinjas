
# Problem statement

""" You are given with an integer k and an array of integers that contain numbers in random order. Write a program
to find k largest numbers from given array. You need to save them in an array and return it.

Time complexity should be O(nlogk) and space complexity should be not more than O(k).

Order of elements in the output is not important. """


# Solution


import heapq  # Importing the heapq module to use heap operations


def kLargest(lst, k):
    """
    Finds the k largest elements in the list `lst` using a min-heap.

    Parameters:
    lst (list): The input list of integers.
    k (int): The number of largest elements to find.

    Returns:
    list: A list containing the k largest elements, arranged as a min-heap.
    """
    # Step 1: Create a min-heap from the first k elements of the list
    heap = lst[:k]
    heapq.heapify(heap)  # Converts the list into a min-heap in O(k) time

    # Step 2: Process the remaining elements in the list
    for i in range(k, len(lst)):
        # If the current element is greater than the smallest element in the heap
        if lst[i] > heap[0]:
            heapq.heappop(heap)  # Remove the smallest element in the heap
            heapq.heappush(heap, lst[i])  # Add the current element to the heap

    # Step 3: Return the k largest elements (stored in the heap)
    return heap


# Input: Read the size of the list
n = int(input())

# Input: Read the list of integers
lst = list(map(int, input().split()))

# Input: Read the value of k
k = int(input())

# Find the k largest elements
ans = kLargest(lst, k)

# Output: Print the k largest elements
print()
print(*ans)
