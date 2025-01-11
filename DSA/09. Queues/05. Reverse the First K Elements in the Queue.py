
# Problem statement

""" For a given queue containing all integer data, reverse the first K elements.
You have been required to make the desired change in the input queue itself. """


# solution


import queue


def reverseQueue(queue, k):
    """
    Reverse the first k elements of the queue while keeping the rest intact.

    Args:
        queue (queue.Queue): The queue to modify.
        k (int): The number of elements to reverse from the front.

    Returns:
        queue.Queue: The modified queue with the first k elements reversed.
    """
    # Step 1: Use a stack to reverse the first k elements
    stack = []

    for i in range(k):
        stack.append(queue.get())  # Pop the first k elements from the queue into the stack

    for i in range(k):
        queue.put(stack.pop())  # Push the elements back from the stack into the queue (reversed order)

    # Step 2: Move the remaining elements (queue size - k) to the back of the queue
    for i in range(queue.qsize() - k):
        queue.put(queue.get())  # Move elements to the back to preserve their original order

    return queue


# Input section
queue = queue.Queue()  # Initialize the queue

n = int(input())

for i in range(n):
    queue.put(int(input()))  # Populate the queue with user input

k = int(input())

# Reverse the first k elements
queue = reverseQueue(queue, k)

# Output the modified queue
while not queue.empty():
    print(queue.get())
