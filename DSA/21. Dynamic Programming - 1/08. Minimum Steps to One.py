
# Problem statement

""" Given a positive integer 'n', find and return the minimum number of steps that 'n' has to take to get reduced to 1.
You can perform any one of the following 3 steps:

1.) Subtract 1 from it. (n = n - ­1) ,
2.) If n is divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 ) ,
3.) If n is divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 ).  """


# Solution


def minStepsToOne(n):
    """
    A recursive function to find the minimum number of steps to reduce a number to 1.
    The allowed operations are:
    1. Subtract 1
    2. Divide by 2 (if divisible)
    3. Divide by 3 (if divisible)
    """

    # Base case: If n is already 1, no steps are needed
    if n == 1:
        return 0

    # If the result for the current value of n is already computed, return it
    if dp[n] != -1:
        return dp[n]

    # Recursive step: Subtract 1
    subtract = minStepsToOne(n - 1)

    # Initialize divide_by_2 and divide_by_3 as infinity (not possible by default)
    divide_by_2 = float('inf')
    divide_by_3 = float('inf')

    # Check divisibility by 2 and compute steps
    if n % 2 == 0:
        divide_by_2 = minStepsToOne(n // 2)

    # Check divisibility by 3 and compute steps
    if n % 3 == 0:
        divide_by_3 = minStepsToOne(n // 3)

    # Find the minimum steps among the three operations
    dp[n] = 1 + min(subtract, divide_by_2, divide_by_3)
    return dp[n]


# Input: The number to reduce to 1
n = int(input())

# Initialize the dp array with -1 to indicate uncomputed values
dp = [-1] * (n + 1)

# Output: Minimum steps to reduce the number to 1
print(minStepsToOne(n))
