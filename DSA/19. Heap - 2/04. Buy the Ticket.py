
# Problem statement

""" You want to buy a ticket for a well-known concert which is happening in your city. But the number of tickets
available is limited. Hence the sponsors of the concert decided to sell tickets to customers based on some priority.

A queue is maintained for buying the tickets and every person is attached with a priority (an integer,
1 being the lowest priority).

The tickets are sold in the following manner -

1. The first person (pi) in the queue requests for the ticket.
2. If there is another person present in the queue who has higher priority than pi, then ask pi to move at
end of the queue without giving him the ticket.
3. Otherwise, give him the ticket (and don't make him stand in queue again).

Giving a ticket to a person takes exactly 1 second and it takes no time for removing and adding a person to the queue.
And you can assume that no new person joins the queue.

Given a list of priorities of N persons standing in the queue and the index of your priority (indexing starts from 0).
Find and return the time it will take until you get the ticket. """


# Solution


import queue  # Importing queue for FIFO operations
import heapq  # Importing heapq for heap operations (max-heap simulation)

def buyTicket(priorities, index):
    """
    Simulates a ticket-buying system where people with higher priority are served first.

    Parameters:
    priorities (list): A list of integers representing the priorities of people in the queue.
    index (int): The index of the person for whom we want to determine the turn.

    Returns:
    int: The turn at which the person at the given index will be served.
    """
    # Step 1: Initialize the queue and max-heap
    q = queue.Queue()  # Queue to store (priority, original index) of each person
    maxHeap = []  # Max-heap (simulated using negative priorities)

    # Fill the queue and max-heap with initial data
    for i in range(len(priorities)):
        q.put((priorities[i], i))  # (priority, index)
        heapq.heappush(maxHeap, -priorities[i])  # Negative priority for max-heap behavior

    count = 0  # Counter to track the number of people served

    # Step 2: Process the queue
    while not q.empty():
        person = q.get()  # Get the first person in the queue

        # Check if this person has the highest priority
        if person[0] == -maxHeap[0]:
            # Serve the person and remove their priority from the max-heap
            heapq.heappop(maxHeap)
            count += 1  # Increment the count of people served

            # If this is the person at the target index, return their turn
            if person[1] == index:
                return count
        else:
            # If this person doesn't have the highest priority, put them back in the queue
            q.put(person)

    return -1  # Should not reach here unless something goes wrong


# Input: Read the list of priorities
priorities = list(map(int, input().split()))

# Input: Read the index of the person for whom the turn is needed
index = int(input())

# Output: Print the turn at which the person at the given index will be served
print(buyTicket(priorities, index))

