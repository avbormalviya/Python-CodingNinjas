
# Problem statement

""" For a given expression in the form of a string, find if there exist any redundant brackets or not. It is given that the expression contains only rounded brackets or parenthesis and the input expression will always be balanced.

A pair of the bracket is said to be redundant when a sub-expression is surrounded by unnecessary or needless brackets.

Example:
Expression: (a+b)+c
Since there are no needless brackets, hence, the output must be 'false'.

Expression: ((a+b))
The expression can be reduced to (a+b). Hence the expression has redundant brackets and the output will be 'true'.
Note:
You will not get a partial score for this problem. You will get marks only if all the test cases are passed.
Return "false" if no brackets are present in the input. """


# solution


def checkRedundantBrackets(expression):
    stack = []  # Initialize an empty stack

    for char in expression:
        # Push opening brackets and operators onto the stack
        if char == '(' or char in '+-*/':
            stack.append(char)
        elif char == ')':  # When a closing bracket is encountered
            hasOperator = False

            # Pop elements until an opening bracket is found
            while stack and stack[-1] != '(':
                top = stack.pop()
                # If an operator is found, set `hasOperator` to True
                if top in '+-*/':
                    hasOperator = True

            # If no operator was found between the brackets, they are redundant
            if not hasOperator:
                return True

            # Pop the opening bracket
            if stack:
                stack.pop()

    # If no redundant brackets are found, return False
    return False


# Testing the checkRedundantBrackets function
expression = input()

# Call the function and print the result
print(checkRedundantBrackets(expression))
