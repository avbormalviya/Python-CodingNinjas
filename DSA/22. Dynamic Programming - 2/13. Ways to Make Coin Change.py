
# Problem statement

""" You are given an infinite supply of coins of each of denominations D = {D0, D1, D2, D3, ...... Dn-1}.
You need to figure out the total number of ways W, in which you can make a change for value V using coins
of denominations from D. Print 0, if a change isn't possible. 1 """


# Solution


def waysToMakeChange(denominations, value, index, dp):
    """
    Function to compute the number of ways to make change for a given value.

    Parameters:
    - denominations: List of available coin denominations.
    - value: The target amount to be made.
    - index: The index in the denominations array to prevent duplicate orderings.
    - dp: Memoization dictionary.

    Returns:
    - The number of unique ways to make change.
    """

    # Base Cases
    if value == 0:
        return 1  # One valid way (select nothing)

    if value < 0 or index >= len(denominations):
        return 0  # No valid way

    # Memoization Key (State is defined by [value, index])
    if (value, index) in dp:
        return dp[(value, index)]

    # Compute ways: Either include current denomination OR skip it
    include = waysToMakeChange(denominations, value - denominations[index], index, dp)  # Stay at index
    exclude = waysToMakeChange(denominations, value, index + 1, dp)  # Move to next index

    # Store and return the computed value
    dp[(value, index)] = include + exclude
    return dp[(value, index)]


# Input Handling
n = int(input())  # Number of denominations
denominations = list(map(int, input().split()))  # Read denominations
v = int(input())  # Target value

# Initialize Memoization Dictionary
dp = {}

# Solve the problem using Recursion + Memoization
print(waysToMakeChange(denominations, v, 0, dp))
