
# Problem statement

""" Given a string S, compute recursively a new string where identical chars that are adjacent in the original string
are separated from each other by a "*". """


# solution


def pairStar(s, index=0):
    """
    Inserts a '*' between consecutive duplicate characters in a string using recursion.

    Parameters:
    scratch_KNN.py (str): The input string.
    index (int): The current index being processed (default is 0).

    Returns:
    str: The modified string with '*' inserted between consecutive duplicates.
    """
    # Base case: If the index is at the last character, return it.
    if index == len(s) - 1:
        return s[index]

    # Recursive case: Process the current character and the rest of the string.
    # If the current character matches the next character, add a '*'.
    if s[index] == s[index + 1]:
        return s[index] + '*' + pairStar(s, index + 1)
    else:
        return s[index] + pairStar(s, index + 1)


# Input: Read the string to modify
input_string = input()

# Output the result
result = pairStar(input_string)
print(result)

