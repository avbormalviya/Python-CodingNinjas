# Problem statement

""" Implement a Stack Data Structure specifically to store integer data using a Singly Linked List.

The data members should be private.

You need to implement the following public functions :

1. Constructor:
It initialises the data members as required.

2. push(data) :
This function should take one argument of type integer. It pushes the element into the stack and returns nothing.

3. pop() :
It pops the element from the top of the stack and in turn, returns the element being popped or deleted. In case the
stack is empty, it returns -1.

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


# Node class to represent a single element in the stack
class Node:
    def __init__(self, data):
        self.data = data  # Stores the data for the node
        self.next = None  # Pointer to the next node in the stack


# Stack class using a linked list
class Stack:
    def __init__(self):
        self.__head = None  # Points to the top node of the stack
        self.__count = 0    # Tracks the number of elements in the stack

    # Pushes a new element onto the stack
    def push(self, data):
        newNode = Node(data)      # Create a new node with the given data
        newNode.next = self.__head  # Link the new node to the current top node
        self.__head = newNode      # Update the top of the stack
        self.__count += 1          # Increment the size counter

    # Removes and returns the top element of the stack
    def pop(self):
        if self.isEmpty():         # Check if the stack is empty
            return -1              # Return -1 if no elements to pop

        popNode = self.__head      # Store the current top node
        self.__head = self.__head.next  # Update the top to the next node
        self.__count -= 1          # Decrement the size counter

        return popNode.data        # Return the data of the popped node

    # Returns the data of the top element without removing it
    def top(self):
        if self.__head is None:    # Check if the stack is empty
            return -1              # Return -1 if no elements in the stack

        return self.__head.data    # Return the data of the top node

    # Returns the number of elements in the stack
    def size(self):
        return self.__count

    # Checks if the stack is empty
    def isEmpty(self):
        return self.__head is None


# Testing the Stack implementation
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

# Pop and print elements until the stack is empty
while not stack.isEmpty():
    print("size --> ", stack.size())
    print("top --> ", stack.top())
    print("is empty --> ", stack.isEmpty())
    print("pop --> ", stack.pop())
    print()

# Final check for empty stack
print("size --> ", stack.size())
print("top --> ", stack.top())
print("is empty --> ", stack.isEmpty())
print("pop --> ", stack.pop())
print()
