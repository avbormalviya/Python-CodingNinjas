
# Problem statement

""" You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check
if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}.
Hence, return true. """


# Solution


def subsetSumToK(n, arr, k, dp):
    # Base Case: If sum (k) becomes 0, we found a valid subset
    if k == 0:
        return True

    # Base Case: If no elements left but k is still > 0, return False
    if n == 0:
        return False

    # If already computed, return stored result to avoid recomputation
    if dp[k] != -1:
        return dp[k] == 1  # Convert int to boolean for correct return type

    # Option 1: Exclude the current element and check if the sum is still possible
    exclude = subsetSumToK(n - 1, arr, k, dp)

    # Option 2: Include the current element if it does not exceed k
    include = False
    if arr[n - 1] <= k:
        include = subsetSumToK(n - 1, arr, k - arr[n - 1], dp)

    # Store the result in the dp array for memoization (1 for True, 0 for False)
    dp[k] = int(exclude or include)

    return dp[k] == 1  # Convert stored value back to boolean


# Read input: Number of elements
n = int(input())

# Read input: Array elements
arr = list(map(int, input().split()))

# Read input: Target sum K
k = int(input())

# Initialize DP array with -1 (indicating uncomputed values)
dp = [-1] * (k + 1)

# Call the function and print the result
print(subsetSumToK(n, arr, k, dp))
