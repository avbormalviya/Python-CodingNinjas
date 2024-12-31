
# Problem statement

""" Write a recursive function to convert a given string into the number it represents. That is input will be a numeric
string that contains only numbers, you need to convert the string into corresponding integer and return the answer. """


# solution


def stringToInteger(str):
    """
    Converts a string representation of a non-negative integer into an integer using recursion.

    Parameters:
    str (str): The input string representing a non-negative integer.

    Returns:
    int: The integer value of the string.
    """

    # Base case 1: If the string is '0', return 0 as the integer value.
    if str == '0':
        return 0

    # Base case 2: If the string length is 1, directly return its integer value.
    if len(str) == 1:
        return int(str)

    # Recursive case: Process the last digit, convert it to integer,
    # and multiply the rest of the string's integer value by 10.
    return int(str[-1]) + 10 * stringToInteger(str[:-1])


# Input: Prompt the user to enter a string representing a non-negative integer.
str = input("Enter a non-negative integer as a string: ")

# Output: Convert the string to an integer and print the result.
print(stringToInteger(str))
