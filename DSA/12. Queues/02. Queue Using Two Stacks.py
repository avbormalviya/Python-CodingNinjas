from os import *
from sys import *
from collections import *
from math import *

class Queue:
    # Stacks to be used in the operations.
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    def enqueue(self, X):
        self.stk1.append(X)

        return True

    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.
    """
    
    def dequeue(self):
        if len(self.stk1) == 0:
            return -1

        while len(self.stk1) > 1:
            self.stk2.append(self.stk1.pop())

        data = self.stk1.pop()

        while len(self.stk2) > 0:
            self.stk1.append(self.stk2.pop())

        return data