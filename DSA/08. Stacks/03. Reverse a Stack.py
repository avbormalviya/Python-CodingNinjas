
# Problem statement

""" You have been given two stacks that can store integers as the data. Out of the two given stacks, one
is populated and the other one is empty. You are required to write a function that reverses the populated
stack using the one which is empty. """


# solution


def reverseStack(inputStack, emptyStack):
    # Base case: If the stack has 0 or 1 element, it's already reversed.
    if len(inputStack) == 0 or len(inputStack) == 1:
        return

    # Step 1: Remove the top element from inputStack and store it in 'x'.
    x = inputStack[-1]
    inputStack.pop()

    # Step 2: Recursively reverse the remaining elements in the inputStack.
    reverseStack(inputStack, emptyStack)

    # Step 3: Move all elements from inputStack to emptyStack, so inputStack becomes empty.
    while len(inputStack) > 0:
        emptyStack.append(inputStack[-1])
        inputStack.pop()

    # Step 4: Add the previously removed element 'x' back to the inputStack.
    inputStack.append(x)

    # Step 5: Move all elements from emptyStack back to inputStack.
    while len(emptyStack) > 0:
        inputStack.append(emptyStack[-1])
        emptyStack.pop()

    return


# Read the input stack from the user as a list of integers
inputStack = list(map(int, input().split()))
emptyStack = list()  # Initialize the helper stack

# Reverse the stack using the reverseStack function
reverseStack(inputStack, emptyStack)

# Print the reversed stack by popping from inputStack
while len(inputStack):
    print(inputStack.pop(), end=" ")
