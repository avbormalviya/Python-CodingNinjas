from sys import stdin


def isBalanced(expression):
    # Use a list as a stack
    stack = []

    for i in expression:
        if i in '([{':
            # Push onto the stack
            stack.append(i)

        elif i in ')]}':
            if not stack:
                # Stack is empty, unbalanced
                return False

            # Pop from the stack
            top = stack.pop()

            if (i == ')' and top != '(') or (i == ']' and top != '[') or (i == '}' and top != '{'):
                # Mismatched parentheses
                return False

                # The expression is balanced if the stack is empty
    return not stack


# main
expression = input().strip()

if isBalanced(expression):
    print("true")
else:
    print("false")