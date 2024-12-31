
# Problem statement

""" Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction
and addition for your calculation. No other operators are allowed. """


# solution


def multiplication(m, n):
    """
    Recursively calculates the product of two integers m and n using addition.

    Parameters:
    m (int): The first number.
    n (int): The second number.

    Returns:
    int: The product of m and n.
    """
    # Base case: If either number is 0, the product is 0
    if m == 0 or n == 0:
        return 0

    if m < n:
        return n + multiplication(m - 1, n)
    else:
        return m + multiplication(m, n - 1)


# Input: Read the numbers m and n
m = int(input())
n = int(input())

# Output the result
print(multiplication(m, n))
