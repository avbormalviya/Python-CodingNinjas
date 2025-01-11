
# Problem statement

""" You need to implement a class for Dequeue i.e. for double ended queue. In this queue, elements can be inserted
and deleted from both the ends.

You don't need to double the capacity.

You need to implement the following functions -

1. constructor
You need to create the appropriate constructor. Size for the queue passed is 10.

2. insertFront -
This function takes an element as input and insert the element at the front of queue. Insert the element only
if queue is not full. And if queue is full, print -1 and return.

3. insertRear -
This function takes an element as input and insert the element at the end of queue. Insert the element only
if queue is not full. And if queue is full, print -1 and return.

4. deleteFront -
This function removes an element from the front of queue. Print -1 if queue is empty.

5. deleteRear -
This function removes an element from the end of queue. Print -1 if queue is empty.

6. getFront -
Returns the element which is at front of the queue. Return -1 if queue is empty.

7. getRear -
Returns the element which is at end of the queue. Return -1 if queue is empty. """


# solution


class Deque:
    def __init__(self, max_size=10):
        """
        Initialize the deque with optional max_size (default is 10).
        """
        self.queue = []  # Internal list to store deque elements
        self.size = 0    # Current size of the deque
        self.max_size = max_size  # Maximum allowed size

    def insertFront(self, data):
        """
        Inserts an element at the front of the deque.
        """
        if self.size < self.max_size:
            self.queue.insert(0, data)
            self.size += 1
        else:
            print("Deque is full! Cannot insert at the front.")

    def insertRear(self, data):
        """
        Inserts an element at the rear of the deque.
        """
        if self.size < self.max_size:
            self.queue.append(data)
            self.size += 1
        else:
            print("Deque is full! Cannot insert at the rear.")

    def deleteFront(self):
        """
        Removes an element from the front of the deque.
        """
        if self.size > 0:
            self.queue.pop(0)
            self.size -= 1
        else:
            print("Deque is empty! Cannot delete from the front.")

    def deleteRear(self):
        """
        Removes an element from the rear of the deque.
        """
        if self.size > 0:
            self.queue.pop()
            self.size -= 1
        else:
            print("Deque is empty! Cannot delete from the rear.")

    def getFront(self):
        """
        Returns the element at the front of the deque.
        """
        if self.size > 0:
            return self.queue[0]
        else:
            return "Deque is empty! No front element."

    def getRear(self):
        """
        Returns the element at the rear of the deque.
        """
        if self.size > 0:
            return self.queue[-1]
        else:
            return "Deque is empty! No rear element."


# Example usage
if __name__ == "__main__":
    q = Deque(5)  # Creating a deque with a maximum size of 5

    q.insertFront(1)
    q.insertFront(2)
    q.insertRear(3)
    q.insertRear(4)
    q.insertRear(5)
    q.insertRear(6)  # Should print "Deque is full!"

    print("Front element:", q.getFront())  # Should print 2
    print("Rear element:", q.getRear())    # Should print 5

    q.deleteFront()
    q.deleteRear()
    print("Front element after deletion:", q.getFront())  # Should print 1
    print("Rear element after deletion:", q.getRear())    # Should print 4

    q.deleteFront()
    q.deleteFront()
    q.deleteFront()  # Should print "Deque is empty!"
