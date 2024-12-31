
# Problem statement

""" Write a recursive function that returns the sum of the digits of a given integer. """


# solution


def sumOfDigits(num):
    """
    Recursively calculates the sum of the digits of a number.

    Parameters:
    num (int): The number whose digits are to be summed.

    Returns:
    int: The sum of the digits of the number.
    """

    # Base case: If the number has only one digit, return it
    if num // 10 == 0:
        return num

    # Recursive call: Sum the digits of the number excluding the last digit
    digits_sum = sumOfDigits(num // 10)

    # Add the last digit of the current number to the result
    return digits_sum + num % 10


# Input: Read the number
n = int(input())

# Output the result
print(sumOfDigits(n))

