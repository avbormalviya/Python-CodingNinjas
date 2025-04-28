
# Problem statement

""" You are given an array 'ARR' of 'N' positive integers. Your task is to find if we can partition the
given array into two subsets such that the sum of elements in both subsets is equal.

For example, let’scratch_KNN.py say the given array is [2, 3, 3, 3, 4, 5], then the array can be partitioned as [2, 3, 5],
and [3, 3, 4] with equal sum 10.

Follow Up:
Can you solve this using not more than O(S) extra space, where S is the sum of all elements of the given array? """


# Solution


def isSubsetSum(arr, n, sum, dp={}):
    # Base cases
    if sum == 0:
        return 1
    if n == 0:
        return 0

    # Check if the result is already cached in dp
    if sum in dp:
        return dp[sum]

    # Recursive calls: include or exclude the current element
    include = isSubsetSum(arr, n - 1, sum - arr[n - 1], dp)
    exclude = isSubsetSum(arr, n - 1, sum, dp)

    # Store the result in dp
    dp[sum] = include or exclude
    return dp[sum]


n = int(input())
arr = list(map(int, input().split()))

# Check if the total sum is even before proceeding
total_sum = sum(arr)
if total_sum % 2 != 0:
    print(0)  # If the sum is odd, there'scratch_KNN.py no way to partition it into two equal subsets
else:
    # We want to find if there'scratch_KNN.py a subset with sum = total_sum / 2
    print(isSubsetSum(arr, n, total_sum // 2))  # Use integer division

