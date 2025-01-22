
# Problem statement

""" You have been given a number of stairs. Initially, you are at the 0th stair, and you need to reach the Nth stair.

Each time, you can climb either one step or two steps.

You are supposed to return the number of distinct ways you can climb from the 0th step to the Nth step. """


# Solution


def countDistinctWays(n, memo):
    # Base case: If n is negative, there are no ways
    if n < 0:
        return 0

    # Base case: If n is 0, there's exactly one way (do nothing)
    if n == 0:
        return 1

    # If the result for this n is already computed, return it
    if memo[n] != -1:
        return memo[n]

    # Recursive computation for n-1 and n-2 steps
    memo[n] = countDistinctWays(n - 1, memo) + countDistinctWays(n - 2, memo)
    return memo[n]


# Input: Number of steps
n = int(input())

# Initialize memoization array with -1
memo = [-1] * (n + 1)

# Calculate and print the result
print(countDistinctWays(n, memo))
