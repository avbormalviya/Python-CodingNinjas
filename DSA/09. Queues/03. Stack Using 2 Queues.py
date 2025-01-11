
# Problem statement

""" Implement a Stack Data Structure specifically to store integer data using two Queues. You have to implement it in such a way that the push operation is done in O(1) time and the pop and top operations are done in O(N) time.

There should be two data members, both being Queues to store the data internally. You may use the inbuilt Queue.

Implement the following public functions :

1. Constructor:
It initialises the data members as required.

2. push(data) :
This function should take one argument of type integer. It pushes the element into the stack and returns nothing.

3. pop() :
It pops the element from the top of the stack and in turn, returns the element being popped or deleted. In case the stack is empty, it returns -1.

4. top :
It returns the element being kept at the top of the stack. In case the stack is empty, it returns -1.

5. size() :
It returns the size of the stack at any given instance of time.

6. isEmpty() :
It returns a boolean value indicating whether the stack is empty or not.

Operations Performed on the Stack:
Query-1(Denoted by an integer 1): Pushes an integer data to the stack.

Query-2(Denoted by an integer 2): Pops the data kept at the top of the stack and returns it to the caller.

Query-3(Denoted by an integer 3): Fetches and returns the data being kept at the top of the stack but doesn't remove it, unlike the pop function.

Query-4(Denoted by an integer 4): Returns the current size of the stack.

Query-5(Denoted by an integer 5): Returns a boolean value denoting whether the stack is empty or not. """


# solution


class Stack:
    def __init__(self):
        # Two queues for stack implementation
        self.q1 = []  # Primary queue
        self.q2 = []  # Secondary queue
        self.size_count = 0  # Maintain stack size

    def push(self, data):
        # Add the new element to q1 and increase the size
        self.q1.append(data)
        self.size_count += 1

    def pop(self):
        # If q1 is empty, the stack is empty
        if not self.q1:
            return -1

        # Transfer all elements from q1 to q2 except the last one
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        # The last element in q1 is the top of the stack, so pop it
        popped_element = self.q1.pop(0)

        # Swap q1 and q2 for the next operation
        self.q1, self.q2 = self.q2, self.q1

        # Decrease the size and return the popped element
        self.size_count -= 1
        return popped_element

    def top(self):
        # If q1 is empty, the stack is empty
        if not self.q1:
            return -1

        # Transfer all elements from q1 to q2 except the last one
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        # The last element in q1 is the top of the stack
        top_element = self.q1.pop(0)

        # Push the top element back to q2 and restore q1 from q2
        self.q2.append(top_element)
        self.q1, self.q2 = self.q2, self.q1

        return top_element

    def size(self):
        # Return the current size of the stack
        return self.size_count

    def isEmpty(self):
        # Check if the stack is empty
        return self.size_count == 0


# Driver code to test the Stack implementation
stack = Stack()

n = int(input())
for _ in range(n):
    query = list(map(int, input().split()))

    if query[0] == 1:  # Push operation
        stack.push(query[1])
    elif query[0] == 2:  # Pop operation
        print(stack.pop())
    elif query[0] == 3:  # Top operation
        print(stack.top())
    elif query[0] == 4:  # Size operation
        print(stack.size())
    elif query[0] == 5:  # isEmpty operation
        print(stack.isEmpty())
