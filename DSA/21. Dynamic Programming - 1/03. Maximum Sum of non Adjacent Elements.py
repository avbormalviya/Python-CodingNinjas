
# Problem statement

""" You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence with
the constraint that no two elements are adjacent in the given array/list.

Note:
A subsequence of an array/list is obtained by deleting some number of elements (can be zero) from the array/list,
leaving the remaining elements in their original order. """


# Solution


def maxSumHelper(arr, i, n, dp):
    # Base case: If we go out of bounds
    if i >= n:
        return 0

    # If already computed, return stored result
    if dp[i] != -1:
        return dp[i]

    # Include the current element and skip the next, or skip the current
    dp[i] = max(arr[i] + maxSumHelper(arr, i + 2, n, dp), maxSumHelper(arr, i + 1, n, dp))

    return dp[i]


def maxSum(arr, n):
    # Edge case: Single element
    if n == 1:
        return arr[0]

    # Initialize dp array with -1 for memoization
    dp = [-1] * n

    # Start calculating from the first index
    return maxSumHelper(arr, 0, n, dp)


# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output result
print(maxSum(arr, n))
