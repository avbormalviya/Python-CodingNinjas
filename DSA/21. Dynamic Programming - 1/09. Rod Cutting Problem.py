
# Problem statement

""" Given a rod of length ‘N’ units. The rod can be cut into different sizes and each size has a cost associated with it. Determine the maximum cost obtained by cutting the rod and selling its pieces.

Note:
1. The sizes will range from 1 to ‘N’ and will be integers.
2. The sum of the pieces cut should be equal to ‘N’.
3. Consider 1-based indexing. """


# Solution


def cutRod(n, prices, dp):
    # Base case: if no length is left, profit is 0
    if n == 0:
        return 0

    # If the result is already calculated, return it (Memoization)
    if dp[n] != -1:
        return dp[n]

    # Initialize max_profit for the current rod length
    max_profit = 0

    # Try cutting the rod into pieces of length 1 to n
    for i in range(1, n + 1):
        # Add the price of the current piece (i-1 because prices is 0-indexed)
        # Recur for the remaining rod length (n - i)
        profit = prices[i - 1] + cutRod(n - i, prices, dp)
        # Update max_profit if this cut yields a higher profit
        max_profit = max(max_profit, profit)

    # Store the result in dp for the current rod length
    dp[n] = max_profit
    return dp[n]


# Input: length of the rod
n = int(input())
# Input: prices of rod pieces of length 1 to n
prices = list(map(int, input().split()))

# Initialize dp array with -1 (to signify uncalculated states)
dp = [-1] * (n + 1)

# Output the maximum profit
print(cutRod(n, prices, dp))
