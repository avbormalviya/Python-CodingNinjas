
# Problem statement

""" Given an integer array (of length n), find and return all the subsets of input array.

NOTE- Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.

Note :
The order of subsets are not important. """


# Solution


def subset(arr, n):
    """
    Generates all subsets of a given list `arr` starting from index `n`.

    Parameters:
    - arr (List[int]): The input list of integers.
    - n (int): The current index being considered.

    Returns:
    - List[List[int]]: A list of lists, where each inner list is a subset.
    """
    # Base Case: If we've considered all elements, return a list containing an empty subset
    if n == len(arr):
        return [[]]

    # Recursive case: Get subsets excluding the current element
    result = subset(arr, n + 1)

    # For each subset generated so far, append the current element `arr[n]`
    for val in result[:]:  # Using slicing to avoid modification during iteration
        result.append([arr[n]] + val)

    return result


# Input handling
n = int(input())
arr = list(map(int, input().split()))

# Generate and print all subsets, each on a new line
print(*subset(arr, 0), sep="\n")
