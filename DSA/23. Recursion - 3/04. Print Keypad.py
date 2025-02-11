# Problem statement

""" Given an integer n, using phone keypad find out and print all the possible strings that can be
made using digits of input n.

Note : The order of strings are not important. Just print different strings in new lines. """

# Solution


# Mobile Keypad mappings for each digit
KEYPAD = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def keypad(n, curr=None):
    """
    Recursively generates all possible strings for a given number `n`
    using mobile keypad character mappings and prints them.

    Parameters:
    - n (int): The input number.
    - curr (List[str]): The current list of combinations built so far.
    """

    # Initialize curr only on the first call to avoid mutable default argument issues
    if curr is None:
        curr = [""]

    # Base Case: When n is reduced to 0, print all combinations
    if n == 0:
        print(*curr, sep="\n")
        return

    # Process remaining digits
    remaining_digits = n // 10
    keypad_chars = KEYPAD[n % 10]  # Get letters corresponding to last digit

    # Generate new combinations by prepending keypad_chars to existing curr list
    keypad(remaining_digits, [prefix + char for prefix in curr for char in keypad_chars])


# Input Handling
n = int(input().strip())

# Generate & Print all possible combinations
keypad(n)
