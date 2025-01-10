
# Problem statement

""" For a given a string expression containing only round brackets or parentheses, check if they are balanced or not. Brackets are said to be balanced if the bracket which opens last, closes first.

Example:
Expression: (()())
Since all the opening brackets have their corresponding closing brackets, we say it is balanced and hence the output will be, 'true'.
You need to return a boolean value indicating whether the expression is balanced or not.

Note:
The input expression will not contain spaces in between. """


# solution


def isBalanced(expression):
    stack = []  # Create an empty stack to hold opening parentheses

    # Iterate through each character in the expression
    for char in expression:
        if char == '(':  # If the character is an opening parenthesis
            stack.append(char)  # Push the opening parenthesis onto the stack
        elif char == ')':  # If the character is a closing parenthesis
            if stack:  # Check if there is an unmatched opening parenthesis in the stack
                stack.pop()  # If the stack is not empty, pop the last opening parenthesis
            else:
                return False  # If the stack is empty, it means there's no matching '(' for this ')'

    # After the loop, check if the stack is empty
    # If the stack is empty, all opening parentheses had matching closing ones, so the expression is balanced
    return not stack  # If stack is empty, return True (balanced), otherwise False (unbalanced)


# Read input expression from the user
expression = input()

# Call the isBalanced function and print the result
print(isBalanced(expression))
