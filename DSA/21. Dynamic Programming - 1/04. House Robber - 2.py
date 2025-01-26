# Problem statement

""" Mr. X is a professional robber planning to rob houses along a street. Each house has a certain amount of
money hidden.



All houses along this street are arranged in a circle. That means the first house is the neighbour of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police
if two adjacent houses are broken into on the same night.



You are given an array/list of non-negative integers 'ARR' representing the amount of money of each house.
Your task is to return the maximum amount of money Mr. X can rob tonight without alerting the police.



Note:
It is possible for Mr. X to rob the same amount of money by looting two different sets of houses.
Just print the maximum possible robbed amount, irrespective of sets of houses robbed.


For example:
(i) Given the input array arr[] = {2, 3, 2} the output will be 3 because Mr X cannot rob house 1 (money = 2) and
then rob house 3 (money = 2), because they are adjacent houses. So, he’ll rob only house 2 (money = 3)

(ii) Given the input array arr[] = {1, 2, 3, 1} the output will be 4 because Mr X rob house 1 (money = 1) and
then rob house 3 (money = 3).

(iii) Given the input array arr[] = {0} the output will be 0 because Mr. X has got nothing to rob. """


# Solution


def robHelper(nums, i, n, dp):
    # Base case: Out of bounds
    if i >= n:
        return 0

    # Use memoized result if available
    if dp[i] != -1:
        return dp[i]

    # Include the current house or skip it
    dp[i] = max(nums[i] + robHelper(nums, i + 2, n, dp), robHelper(nums, i + 1, n, dp))
    return dp[i]


def rob(nums, n):
    # Edge case: Only one house
    if n == 1:
        return nums[0]

    # Function to calculate max loot for a specific range
    def robRange(nums, start, end):
        dp = [-1] * (end - start + 1)
        return robHelper(nums, 0, end - start + 1, dp)

    # Maximum loot:
    # 1. Robbing from house 0 to house n-2
    # 2. Robbing from house 1 to house n-1
    return max(robRange(nums[:-1], 0, n - 2), robRange(nums[1:], 1, n - 1))


# Input and Output
n = int(input())
arr = list(map(int, input().split()))

print(rob(arr, n))
