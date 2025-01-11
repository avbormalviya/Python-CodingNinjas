
# Problem statement

""" You will be given ‘Q’ queries. You need to implement a queue using two stacks according to those queries. Each query
will belong to one of these three types:

1 ‘X’: Enqueue element ‘X’  into the end of the nth queue. Returns true after the element is enqueued.

2: Dequeue the element at the front of the nth queue. Returns -1 if the queue is empty, otherwise, returns the
dequeued element.

Note:
Enqueue means adding an element to the end of the queue, while Dequeue means removing the element from the front of
the queue. """


# solution


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)
        return True

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return -1  # Queue is empty

        return self.stack2.pop()


queue = Queue()

n = int(input())
for _ in range(n):
    query = list(map(int, input().split()))

    if query[0] == 1:  # Enqueue operation
        print(queue.enqueue(query[1]))
    elif query[0] == 2:  # Dequeue operation
        print(queue.dequeue())
