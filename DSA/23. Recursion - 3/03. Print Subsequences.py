
# Problem statement

""" Given a string (lets say of length n), print all the subsequences of the given string.

Subsequences contain all the strings of length varying from 0 to n. But the order of characters
should remain same as in the input string.

Note :
The order of subsequences are not important. Print every subsequence in new line. """


# Solution


def subsequences(s, index=0, curr=""):
    """
    Recursively prints all subsequences of the string `s`.

    Parameters:
    - s: The input string.
    - index: The current position in the string (default is 0).
    - curr: The current subsequence being built (default is an empty string).
    """

    # Base Case: When we've considered all characters in the string,
    # print the current subsequence (which may be empty) and return.
    if index == len(s):
        print(curr)
        return

    # Recursive Call 1 (Include):
    # Add the current character s[index] to the current subsequence (curr)
    # and recursively process the remainder of the string.
    subsequences(s, index + 1, curr + s[index])

    # Recursive Call 2 (Exclude):
    # Do not add the current character, and recursively process the remainder
    # of the string while keeping the current subsequence unchanged.
    subsequences(s, index + 1, curr)


# Read the input string from the user and remove any leading/trailing whitespace.
s = input().strip()

# Start the recursive process to generate and print all subsequences.
subsequences(s)
