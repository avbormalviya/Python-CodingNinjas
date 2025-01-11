
# Problem statement

""" You have been given a queue that can store integers as the data. You are required to write a function that reverses
the populated queue itself without using any other data structures. """


# solution


import queue


def reverseQueue(queue):
    """
    Recursively reverse the given queue.
    Args:
        queue (queue.Queue): The queue to reverse.
    """
    # Base case: If the queue is empty, stop recursion
    if queue.empty():
        return

    # Step 1: Remove the front element from the queue
    data = queue.get()

    # Step 2: Recursively reverse the rest of the queue
    reverseQueue(queue)

    # Step 3: Add the removed element back to the rear of the queue
    queue.put(data)


# Input section
queue = queue.Queue()  # Initialize an empty queue

n = int(input())

for _ in range(n):
    queue.put(int(input()))  # Populate the queue with user input

# Reverse the queue
reverseQueue(queue)

# Output the reversed queue
while not queue.empty():
    print(queue.get())
