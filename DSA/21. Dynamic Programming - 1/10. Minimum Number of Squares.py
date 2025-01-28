
# Problem statement

""" A number can always be represented as a sum of squares of other numbers. Note that 1 is a square
and we can always break a number as [(1 * 1) + (1 * 1) + (1 * 1) + …]. Given a number n, find the
 minimum number of squares that sum to n. """


# Solution


def minSquares(n, dp={}):
    # Base case: if n is 0, no squares are needed
    if n == 0:
        return 0

    # If the result for n is already computed, return it
    if n in dp:
        return dp[n]

    # Initialize the minimum count to infinity
    min_count = float('inf')

    # Try every possible square less than or equal to n
    for i in range(1, int(n ** 0.5) + 1):
        # Recursive call for the remaining value (n - i^2)
        res = minSquares(n - i * i, dp) + 1
        # Update the minimum count if a smaller result is found
        min_count = min(min_count, res)

    # Store the result in the dp dictionary
    dp[n] = min_count
    return dp[n]


# Input: Number to find minimum squares for
n = int(input())
# Output: Minimum number of squares that sum to n
print(minSquares(n))
