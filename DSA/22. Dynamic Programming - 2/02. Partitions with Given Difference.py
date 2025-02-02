
# Problem statement

""" Given an array ‘ARR’, partition it into two subsets (possibly empty) such that their union is the original array.
Let the sum of the elements of these two subsets be ‘S1’ and ‘S2’.

Given a difference ‘D’, count the number of partitions in which ‘S1’ is greater than or equal to ‘S2’ and
the difference between ‘S1’ and ‘S2’ is equal to ‘D’. Since the answer may be too large, return it modulo ‘10^9 + 7’.

If ‘Pi_Sj’ denotes the Subset ‘j’ for Partition ‘i’. Then, two partitions P1 and P2 are considered different if:

1) P1_S1 != P2_S1 i.e, at least one of the elements of P1_S1 is different from P2_S2.
2) P1_S1 == P2_S2, but the indices set represented by P1_S1 is not equal to the indices set of P2_S2. Here,
the indices set of P1_S1 is formed by taking the indices of the elements from which the subset is formed.
Refer to the example below for clarification.
Note that the sum of the elements of an empty subset is 0.

For example :
If N = 4, D = 3, ARR = {5, 2, 5, 1}
There are only two possible partitions of this array.
Partition 1: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
Partition 2: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
These two partitions are different because, in the 1st partition, S1 contains 5 from index 0, and in the 2nd partition,
S1 contains 5 from index 2. """


# Solution


MOD = 10 ** 9 + 7


def partitions_with_given_difference(arr, diff, sum1, sum2, n, memo):
    # Base case: If we've processed all elements
    if n == 0:
        return 1 if (sum1 - sum2) == diff else 0

    # Check if the result for this state is already computed
    if (abs(sum1 - sum2)) in memo:
        return memo[abs(sum1 - sum2)]

    # Include or exclude the current element
    include = partitions_with_given_difference(arr, diff, sum1 + arr[n - 1], sum2, n - 1, memo)
    exclude = partitions_with_given_difference(arr, diff, sum1, sum2 + arr[n - 1], n - 1, memo)

    # Save the result in memo and return the result modulo MOD
    memo[abs(sum1 - sum2)] = (include + exclude) % MOD
    return memo[abs(sum1 - sum2)]


# Input
n = int(input())
arr = list(map(int, input().split()))
diff = int(input())

# Memoization dictionary
memo = {}

# Call the recursive function
result = partitions_with_given_difference(arr, diff, 0, 0, len(arr), memo)
print(result)

