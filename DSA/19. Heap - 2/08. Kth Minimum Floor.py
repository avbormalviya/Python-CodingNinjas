
# Problem statement

""" Ninja is appointed as an architect in Square City. As the name suggests, all the ‘N’ * ‘N’ buildings in
 the Square City are constructed in a square grid with ‘N’ rows and ‘N’ columns. Each building has a fixed
 number of floors and is arranged in a row and column in non decreasing order of the number of floors.

Ninja wants to develop the Square City. So, he selects the ‘K’the building with minimum floors and plans to work on it.
As he is busy deciding the design and infrastructure for that building, he asks you for help.

Can you help Ninja find the building with ‘K’the building with minimum floors? """


# Solution


import heapq  # Importing heapq for heap operations


def kthSmallest(matrix, n, k):
    """
    Finds the k-th smallest element in an n x n matrix where each row and column is sorted.

    Parameters:
    matrix (list of lists): The n x n matrix (sorted rows and columns).
    n (int): The size of the matrix (n x n).
    k (int): The k-th position to find the smallest element.

    Returns:
    int: The k-th smallest element in the matrix.
    """
    # Min-heap to store the elements in sorted order
    heap = []

    # Push the first element of each row into the heap
    # Each element in the heap is a tuple: (value, row, col)
    for i in range(n):
        heapq.heappush(heap, (matrix[i][0], i, 0))

    # Extract the smallest elements from the heap k times
    for _ in range(k - 1):
        val, row, col = heapq.heappop(heap)  # Get the smallest element
        # If there's a next column in the same row, add it to the heap
        if col + 1 < n:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

    # The top of the heap now contains the k-th smallest element
    return heapq.heappop(heap)[0]


# Input: Size of the matrix
n = int(input())

# Input: The n x n matrix
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Input: The k-th position
k = int(input())

# Output: Print the k-th smallest element in the matrix
print(kthSmallest(matrix, n, k))
