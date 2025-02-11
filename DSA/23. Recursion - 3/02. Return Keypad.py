
# Problem statement

""" Given an integer n, using phone keypad find out and return all the possible strings that can be
made using digits of input n.

Note : The order of strings are not important. """


# Solution


# Mapping of digits to corresponding characters on a mobile keypad
KEYPAD = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def keypad(n):
    """
    Recursively generates all possible strings for a given number `n`
    using mobile keypad character mappings.

    Parameters:
    - n (int): The input number.

    Returns:
    - List[str]: A list of all possible character combinations.
    """

    # Base Case: If n is 0, return an empty string as the only possibility
    if n == 0:
        return [""]

    # Recursive Call: Get all combinations for the smaller number (excluding last digit)
    small_output = keypad(n // 10)

    # Get the corresponding string for the last digit of `n`
    keypad_chars = KEYPAD[n % 10]

    # Generate all possible combinations using list comprehension
    return [prefix + char for prefix in small_output for char in keypad_chars]


# Input Handling
n = int(input().strip())

# Print each combination on a new line
print(*keypad(n), sep="\n")
