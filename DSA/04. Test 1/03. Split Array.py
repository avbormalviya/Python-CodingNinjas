
# Problem statement

""" Given an integer array A of size N, check if the input array can be divided in two groups G1 and G2 with
following properties-

- Sum of both group elements are equal
- Group 1: All elements in the input, which are divisible by 5
- Group 2: All elements in the input, which are divisible by 3 (but not divisible by 5).
- Elements which are neither divisible by 5 nor by 3, can be put in either group G1 or G2 to satisfy the equal
sum property.

Group 1 and Group 2 are allowed to be unordered and all the elements in the Array A must belong to only one of
the groups.

Return true, if array can be split according to the above rules, else return false. """


# solution

def splitArray(arr, lSum, rSum, curr):
    """
    Recursive function to determine if an array can be split into two groups with equal sums.

    :param arr: List of integers
    :param lSum: Sum of the left group
    :param rSum: Sum of the right group
    :param curr: Current index in the array
    :return: True if the array can be split as described, otherwise False
    """
    # Base case: If we have processed all elements
    if curr == len(arr):
        return lSum == rSum

    # If the current element is divisible by 5, add it to the left group
    if arr[curr] % 5 == 0:
        return splitArray(arr, lSum + arr[curr], rSum, curr + 1)

    # If the current element is divisible by 3 (but not 5), add it to the right group
    if arr[curr] % 3 == 0:
        return splitArray(arr, lSum, rSum + arr[curr], curr + 1)

    # If the current element is neither divisible by 5 nor 3, try both possibilities
    # Option 1: Add the current element to the left group
    left = splitArray(arr, lSum + arr[curr], rSum, curr + 1)
    # Option 2: Add the current element to the right group
    right = splitArray(arr, lSum, rSum + arr[curr], curr + 1)

    # Return True if either option leads to a valid split
    return left or right


# Input size of the array
n = int(input())

# Input array elements
arr = list(map(int, input().split()))

# Output result
print(splitArray(arr, 0, 0, 0))
