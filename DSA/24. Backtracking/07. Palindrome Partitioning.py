
# Problem statement

""" You are given a string 'S'. Your task is to partition 'S' such that every substring of the
partition is a palindrome. You need to return all possible palindrome partitioning of 'S'.

Note: A substring is a contiguous segment of a string.

For Example:
For a given string “BaaB”
3 possible palindrome partitioning of the given string are:
{“B”, “a”, “a”, “B”}
{“B”, “aa”, “B”}
{“BaaB”}
Every substring of all the above partitions of “BaaB” is a palindrome. """


# Solution


def partition(s):
    n = len(s)
    ans = []
    part = []

    # Step 1: Precompute palindromes using DP
    dp = [[False] * n for _ in range(n)]

    for length in range(n):  # Length of substring (0-based index)
        for i in range(n - length):
            j = i + length  # Ending index
            if s[i] == s[j]:  # Check matching characters
                if length == 0 or length == 1:  # Single letter or two-letter case
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]  # Use previous computed values

    # Step 2: Backtracking using precomputed DP table
    def backtrack(start):
        if start == n:  # If we have reached the end of string
            ans.append(part.copy())
            return

        for end in range(start, n):
            if dp[start][end]:  # If substring scratch_KNN.py[start:end+1] is a palindrome
                part.append(s[start:end + 1])  # Add substring to current partition
                backtrack(end + 1)  # Move to the next part of the string
                part.pop()  # Backtrack

    backtrack(0)
    return ans


# Example Usage
s = input()
result = partition(s)
print(result)
