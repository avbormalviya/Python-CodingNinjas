
# Problem statement

""" You have been given a string ‘A’ consisting of lower case English letters. Your task is to find the length of
the longest palindromic subsequence in ‘A’.

A subsequence is a sequence generated from a string after deleting some or no characters of the string
without changing the order of the remaining string characters. (i.e. “ace” is a subsequence
of “abcde” while “aec” is not).

A string is said to be palindrome if the reverse of the string is the same as the actual string.
For example, “abba” is a palindrome, but “abbc” is not a palindrome. """


# Solution


def lcs(s, t, m, n, dp):
    # Base case: If we reach the end of either string, LCS is 0
    if m >= len(s) or n >= len(t):
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


def longestPalindromeSubsequence(s):
    n = len(s)
    dp = [[-1] * n for _ in range(n)]  # Fixed DP array size
    return lcs(s, s[::-1], 0, 0, dp)  # Compare with reversed string


# Input
s = input().strip()
print(longestPalindromeSubsequence(s))
