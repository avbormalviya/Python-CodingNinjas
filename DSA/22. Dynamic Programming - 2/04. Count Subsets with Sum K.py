
# Problem statement

""" You are given an array 'arr' of size 'n' containing positive integers and a target sum 'k'.

Find the number of ways of selecting the elements from the array such that the sum of chosen elements is
equal to the target 'k'.

Since the number of ways can be very large, print it modulo 10 ^ 9 + 7.

Example:
Input: 'arr' = [1, 1, 4, 5]
Output: 3

Explanation: The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently. """


# Solution


MOD = 10 ** 9 + 7


def countSubsetsWithSumK(arr, n, k, dp):
    if k == 0:
        return 1  # Empty subset sums to 0

    if n == 0:
        return 0  # No elements left

    if (n, k) in dp:
        return dp[(n, k)]  # Memoized result

    # Exclude current element
    exclude = countSubsetsWithSumK(arr, n - 1, k, dp)

    # Include current element (only if k >= arr[n-1])
    include = 0
    if k >= arr[n - 1]:
        include = countSubsetsWithSumK(arr, n - 1, k - arr[n - 1], dp)

    dp[(n, k)] = exclude + include  # Memoize result
    return dp[(n, k)]


# Input Handling
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

dp = {}  # Dictionary for memoization

print(countSubsetsWithSumK(arr, n, k, dp))
