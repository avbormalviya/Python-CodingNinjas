
# Problem statement

""" Given k, find the geometric sum i.e.
1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k)

Note :
using recursion. """


# solution


def geometricSum(k):
    """
    Calculates the geometric sum of the series:
    1 + 1/2 + 1/4 + ... + 1/(2^k) using recursion.

    Parameters:
    k (int): The number of terms in the series (0-based index).

    Returns:
    float: The sum of the series up to the kth term.
    """

    # Base case: The sum of the series when k = 0 is 1
    if k == 0:
        return 1

    # Recursive case: Add 1/(2^k) to the sum of the series up to (k-1)
    return 1 / (2 ** k) + geometricSum(k - 1)


# Input: Read the value of k (number of terms - 1)
n = int(input())

# Output the result
print(geometricSum(n))
