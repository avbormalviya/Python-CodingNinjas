
# Problem statement

""" For a given array with N elements, you need to find the length of the longest subsequence from the array
such that all the elements of the subsequence are sorted in strictly increasing order.

Strictly Increasing Sequence is when each term in the sequence is larger than the preceding term.

For example:
[1, 2, 3, 4] is a strictly increasing array, while [2, 1, 4, 3] is not. """


# Solution


def lis_recursive(arr, n, i, prev):
    if i == n:
        return 0  # Base case: End of array

    # Option 1: Skip current element
    exclude = lis_recursive(arr, n, i + 1, prev)

    # Option 2: Include current element (only if it's increasing)
    include = 0
    if prev == -1 or arr[i] > arr[prev]:
        include = 1 + lis_recursive(arr, n, i + 1, i)

    return max(include, exclude)


def longestIncreasingSubsequence(arr, n):
    dp = [-1] * n  # 1D DP array (not used for memoization, but optimization)

    max_lis = 0
    for i in range(n):
        max_lis = max(max_lis, lis_recursive(arr, n, i, -1))

    return max_lis


# Input
n = int(input())
arr = list(map(int, input().split()))

print(longestIncreasingSubsequence(arr, n))
