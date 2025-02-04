
# Problem statement

""" A thief is robbing a store and can carry a maximal weight of W into his knapsack. There are N items and the
ith item weighs wi and is of value vi. Considering the constraints of the maximum weight that a knapsack can carry,
you have to find and return the maximum value that a thief can generate by stealing items. """


# Solution


def knapsack(W, wt, val, n, dp):
    if W == 0 or n == 0:
        return 0

    if dp[W] != -1:  # Memoization check
        return dp[W]

    # Exclude current item
    exclude = knapsack(W, wt, val, n - 1, dp)

    # Include current item (only if weight is within the limit)
    include = 0
    if W >= wt[n - 1]:
        include = knapsack(W - wt[n - 1], wt, val, n - 1, dp) + val[n - 1]

    dp[W] = max(include, exclude)  # Memoize result
    return dp[W]


# Input Handling
n = int(input())
wt = list(map(int, input().split()))
val = list(map(int, input().split()))
W = int(input())

dp = [-1] * (W + 1)  # 1D DP array for memoization

print(knapsack(W, wt, val, n, dp))
