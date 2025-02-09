
# Problem statement

""" You are given an array ‘ARR’ of ‘N’ integers and a target number, ‘TARGET’. Your task is to build an expression out of an array by adding one of the symbols '+' and '-' before each integer in an array, and then by concatenating all the integers, you want to achieve a target. You have to return the number of ways the target can be achieved.

For Example :
You are given the array ‘ARR’ = [1, 1, 1, 1, 1], ‘TARGET’ = 3. The number of ways this target can be achieved is:
1. -1 + 1 + 1 + 1 + 1 = 3
2. +1 - 1 + 1 + 1 + 1 = 3
3. +1 + 1 - 1 + 1 + 1 = 3
4. +1 + 1 + 1 - 1 + 1 = 3
5. +1 + 1 + 1 + 1 - 1 = 3
These are the 5 ways to make. Hence the answer is 5. """


# Solution


def targetSum(arr, target, index=0, dp={}):
    """
    Function to count the number of ways to assign + or - to elements of `arr`
    so that their sum equals `target`.

    Parameters:
    - arr: List of integers.
    - target: The required target sum.
    - index: Current index in the array.
    - dp: Memoization dictionary storing (index, target) results.

    Returns:
    - Number of ways to achieve the target sum.
    """

    # Base case: If we have processed all elements
    if index == len(arr):
        return 1 if target == 0 else 0  # Valid sum found if target is 0

    # Memoization check (storing results based on index and target)
    if (index, target) in dp:
        return dp[(index, target)]

    # Try adding and subtracting the current element
    add = targetSum(arr, target - arr[index], index + 1, dp)
    subtract = targetSum(arr, target + arr[index], index + 1, dp)

    # Store result in dp table
    dp[(index, target)] = add + subtract
    return dp[(index, target)]


# Input Handling
n = int(input())  # Number of elements
arr = list(map(int, input().split()))  # Read array
target = int(input())  # Target sum

# Solve the problem
print(targetSum(arr, target))
