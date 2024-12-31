
# Problem statement

""" Given an integer N, count and return the number of zeros that are present in the given integer using recursion. """


# solution


def countZeros(number):
    """
    Recursively counts the number of zeros in a given integer.

    Parameters:
    number (int): The number in which zeros are to be counted.

    Returns:
    int: The count of zeros in the number.
    """

    # Base case: If the number is 0, it contains 1 zero
    if number == 0:
        return 1

    # Handle negative numbers by converting them to positive
    if number < 0:
        number = -number

    # Base case: Single-digit numbers other than 0 have no zeros
    if number < 10:
        return 0

    # Recursive case: Check if the last digit is zero and process the rest of the number
    if number % 10 == 0:
        return 1 + countZeros(number // 10)
    else:
        return countZeros(number // 10)


# Input: Read an integer from the user
n = int(input())

# Output: Print the count of zeros in the number
print(countZeros(n))

