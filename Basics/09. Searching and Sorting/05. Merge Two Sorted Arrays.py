# Problem statement

""" You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively, merge them into a third
array/list such that the third array is also sorted.

Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
0 <= M <= 10^5

Time Limit: 1 sec

Note:
Consider the case when size of the two arrays is not same. """

# solution


from typing import List


def mergeTwoSortedArrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """Merge two sorted arrays into one sorted array."""
    arr3 = []
    i, j = 0, 0

    # Merge elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    # Add remaining elements from arr1, if any
    arr3.extend(arr1[i:])

    # Add remaining elements from arr2, if any
    arr3.extend(arr2[j:])

    return arr3


# Input Handling
n = int(input())
arr1 = [int(input()) for i in range(n)]

m = int(input())
arr2 = [int(input()) for i in range(m)]

# Call the function and print the result
print(mergeTwoSortedArrays(arr1, arr2))
