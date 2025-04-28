
# Problem statement

""" We have a collection of 'N' stones, each stone has a positive integer weight.

On each turn, we choose the two heaviest stones and smash them together. Suppose the stones have weights 'x' and 'y'
with 'x' <= 'y'. The result of this smash will be:

1. If 'x' == 'y', both stones are totally destroyed;

2. If 'x' != 'y', the stone of weight 'x' is totally destroyed, and the stone of weight 'y' has a
new weight equal to 'y - x'.

In the end, there is at most 1 stone left. Return the weight of this stone or 0 if there are no stones left. """


# Solution

import heapq  # Importing the heapq module for heap operations

def lastStoneWeight(stones):
    """
    Simulates the process of smashing stones and returns the weight of the last remaining stone.

    Parameters:
    stones (list): A list of integers representing the weights of the stones.

    Returns:
    int: The weight of the last remaining stone, or 0 if no stones are left.
    """
    # Step 1: Convert all stone weights to negative
    # Using a max-heap by storing negative weights, since Python'scratch_KNN.py heapq is a min-heap by default
    heap = [-stone for stone in stones]
    heapq.heapify(heap)  # Heapify the negative weights to create a max-heap

    # Step 2: Process the heap until one or no stones remain
    while len(heap) > 1:
        # Remove the two heaviest stones (largest in the max-heap)
        x = -heapq.heappop(heap)  # Heaviest stone (convert back to positive)
        y = -heapq.heappop(heap)  # Second heaviest stone (convert back to positive)

        # If the stones have different weights, push the difference back into the heap
        if x != y:
            heapq.heappush(heap, -abs(y - x))  # Store the negative of the difference

    # Step 3: Return the weight of the last stone, or 0 if the heap is empty
    return 0 if not heap else -heap[0]


# Input: Read the number of stones
n = int(input())

# Input: Read the list of stone weights
stones = list(map(int, input().split()))

# Calculate the weight of the last stone
ans = lastStoneWeight(stones)

# Output: Print the weight of the last remaining stone
print(ans)
