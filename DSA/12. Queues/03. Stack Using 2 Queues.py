from sys import stdin

import queue


class Stack:

    # Define data members and __init__()
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        # Implement the getSize() function
        return self.q1.qsize()

    def isEmpty(self):
        # Implement the isEmpty() function
        return self.q1.empty()

    def push(self, data):
        # Implement the push(element) function
        self.q1.put(data)

    def pop(self):
        # Implement the pop() function
        if self.q1.qsize() == 0:
            return -1

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        ans = self.q1.get()

        self.q1, self.q2 = self.q2, self.q1

        return ans

    def top(self):
        if self.q1.qsize() == 0:
            return -1

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        ans = self.q1.get()

        self.q2.put(ans)
        self.q1, self.q2 = self.q2, self.q1

        return ans


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1