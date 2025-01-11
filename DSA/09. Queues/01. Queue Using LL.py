
# Problem statement

""" Implement a Queue Data Structure specifically to store integer data using a Singly Linked List.

The data members should be private.

You need to implement the following public functions :

1. Constructor:
It initialises the data members as required.

2. enqueue(data) :
This function should take one argument of type integer. It enqueues the element into the queue and returns nothing.

3. dequeue() :
It dequeues/removes the element from the front of the queue and in turn, returns the element being dequeued or removed.
In case the queue is empty, it returns -1.

4. front() :
It returns the element being kept at the front of the queue. In case the queue is empty, it returns -1.

5. getSize() :
It returns the size of the queue at any given instance of time.

6. isEmpty() :
It returns a boolean value indicating whether the queue is empty or not.

Operations Performed on the Stack:
Query-1(Denoted by an integer 1): Enqueues an integer data to the queue.

Query-2(Denoted by an integer 2): Dequeues the data kept at the front of the queue and returns it to the caller.

Query-3(Denoted by an integer 3): Fetches and returns the data being kept at the front of the queue but doesn't remove
it, unlike the dequeue function.

Query-4(Denoted by an integer 4): Returns the current size of the queue.

Query-5(Denoted by an integer 5): Returns a boolean value denoting whether the queue is empty or not. """


# solution


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        # Initialize front and rear pointers and size of the queue
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        # Add a new node with the given data to the rear of the queue
        new_node = Node(data)

        if self.front is None:  # Queue is empty
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node  # Link the new node at the rear
            self.rear = new_node  # Update the rear pointer

        self.size += 1  # Increment the size of the queue

    def dequeue(self):
        # Remove and return the front element of the queue
        if self.front is None:  # Queue is empty
            return -1

        data = self.front.data  # Store the data to return
        self.front = self.front.next  # Move the front pointer forward
        self.size -= 1  # Decrement the size of the queue

        if self.front is None:  # Queue becomes empty
            self.rear = None

        return data

    def getFront(self):  # Renamed from 'front' to 'getFront' to avoid naming conflict
        # Return the front element of the queue without removing it
        if self.front is None:  # Queue is empty
            return -1

        return self.front.data

    def getSize(self):
        # Return the current size of the queue
        return self.size

    def isEmpty(self):
        # Check if the queue is empty
        return self.size == 0


# Driver code to test the Queue implementation
queue = Queue()

n = int(input())
for _ in range(n):
    query = list(map(int, input().split()))

    if query[0] == 1:  # Enqueue operation
        queue.enqueue(query[1])
    elif query[0] == 2:  # Dequeue operation
        print(queue.dequeue())
    elif query[0] == 3:  # Get front element
        print(queue.getFront())
    elif query[0] == 4:  # Get size of the queue
        print(queue.getSize())
    elif query[0] == 5:  # Check if the queue is empty
        print(queue.isEmpty())
