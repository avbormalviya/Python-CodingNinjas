
# Problem statement

""" For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to
make the expression balanced. The expression will only contain curly brackets.

If the expression can't be balanced, return -1.

Example:
Expression: {{{{
If we reverse the second and the fourth opening brackets, the whole expression will get balanced. Since we have to
reverse two brackets to make the expression balanced, the expected output will be 2.

Expression: {{{
In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and
hence will not be able to make the expression balanced and the output will be -1. """


# solution


def minBracketReversals(expression):
    # If the length of the expression is odd, it is impossible to balance
    if len(expression) % 2 != 0:
        return -1

    open_count = 0   # Count of unmatched '{'
    close_count = 0  # Count of unmatched '}'

    # Traverse the expression
    for char in expression:
        if char == '{':
            open_count += 1
        elif char == '}':
            if open_count > 0:  # Match with an unmatched '{'
                open_count -= 1
            else:
                close_count += 1  # Unmatched '}'

    # Calculate the number of reversals needed
    # Divide counts by 2 to handle pairs, using (x + 1) // 2 for ceiling division
    reversals = (open_count + 1) // 2 + (close_count + 1) // 2

    return reversals


expression = input()
print(minBracketReversals(expression))
