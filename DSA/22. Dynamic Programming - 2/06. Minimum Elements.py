
# Problem statement

""" You are given an array of ‘N’ distinct integers and an integer ‘X’ representing the target sum. You have to tell the minimum number of elements you have to take to reach the target sum ‘X’.

Note:
You have an infinite number of elements of each type.

For example
If N=3 and X=7 and array elements are [1,2,3].

Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.

Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
Hence the output is 3. """


# Solution


def minimumElements(nums, n, x, dp={}):
    if x == 0:
        return 0  # No steps needed if the target is 0

    if x in dp:
        return dp[x]  # Return memoized result

    minStep = float('inf')  # Initialize to infinity

    for i in range(n):  # Iterate over all elements
        if x >= nums[i]:  # If the current number can be used
            minStep = min(minStep, minimumElements(nums, n, x - nums[i], dp) + 1)

    # If minStep is still infinity, no solution exists, return -1
    dp[x] = minStep if minStep != float('inf') else -1
    return dp[x]


# Input Handling
n = int(input())
nums = list(map(int, input().split()))
x = int(input())

print(minimumElements(nums, n, x))
