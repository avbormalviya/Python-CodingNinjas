
# Problem statement

""" Given two strings, 'S' and 'T' with lengths 'M' and 'N', find the length of the 'Longest Common Subsequence'.

For a string 'str'(per se) of length K, the subsequences are the strings containing characters in the same relative
order as they are present in 'str,' but not necessarily contiguous. Subsequences contain all the strings of
length varying from 0 to K.

Example :
Subsequences of string "abc" are:  ""(empty string), a, b, c, ab, bc, ac, abc. """


# Solution

def lcs(s, t, m, n, dp):
    # Base case: if we reach the end of either string, LCS is 0
    if m == len(s) or n == len(t):
        return 0

    # Return memoized result if already computed
    if dp[m][n] != -1:
        return dp[m][n]

    # If characters match, move both indices forward
    if s[m] == t[n]:
        dp[m][n] = 1 + lcs(s, t, m + 1, n + 1, dp)
    else:
        # Otherwise, take the max of moving forward in either string
        dp[m][n] = max(lcs(s, t, m + 1, n, dp), lcs(s, t, m, n + 1, dp))

    return dp[m][n]


# Input
s = input()
t = input()

# DP table initialized with -1
dp = [[-1] * (len(t) + 1) for _ in range(len(s) + 1)]

# Compute and print LCS length
print(lcs(s, t, 0, 0, dp))
