
# Problem statement

""" Given two strings, ‘A’ and ‘B’. Return the shortest supersequence string ‘S’, containing both ‘A’ and ‘B’ as its subsequences. If there are multiple answers, return any of them.

Note: A string 's' is a subsequence of string 't' if deleting some number of characters from 't' (possibly 0) results in the string 's'.

For example:
Suppose ‘A’ = “brute”, and ‘B’ = “groot”

The shortest supersequence will be “bgruoote”. As shown below, it contains both ‘A’ and ‘B’ as subsequences.

A   A A     A A
b g r u o o t e
  B B   B B B

It can be proved that the length of supersequence for this input cannot be less than 8.
So the output will be bgruoote. """


# Solution


def lcs(s, t, m, n, dp):
    """
    Function to compute the Longest Common Subsequence (LCS) length using recursion + memoization.

    Parameters:
    - s: First string.
    - t: Second string.
    - m: Current index in s.
    - n: Current index in t.
    - dp: Memoization table.

    Returns:
    - Length of LCS.
    """

    # Base case: If either string is exhausted, LCS is 0
    if m == len(s) or n == len(t):
        return 0

    # Return precomputed result if available
    if dp[m][n] != -1:
        return dp[m][n]

    # Case 1: Characters match → Move both indices forward
    if s[m] == t[n]:
        dp[m][n] = 1 + lcs(s, t, m + 1, n + 1, dp)

    # Case 2: Characters don't match → Take the maximum LCS from two choices
    else:
        dp[m][n] = max(lcs(s, t, m + 1, n, dp), lcs(s, t, m, n + 1, dp))

    return dp[m][n]


# Input Handling
A = input().strip()  # Read first string
B = input().strip()  # Read second string

# Initialize DP table with -1 (to indicate uncomputed values)
dp = [[-1] * (len(B) + 1) for _ in range(len(A) + 1)]

# Compute the Shortest Common Supersequence Length
scs_length = len(A) + len(B) - lcs(A, B, 0, 0, dp)

# Output result
print(scs_length)
