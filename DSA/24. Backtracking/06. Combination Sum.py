
# Problem statement

""" You are given an array 'ARR' of 'N' distinct positive integers. You are also given a non-negative integer 'B'.

Your task is to return all unique combinations in the array whose sum equals 'B'.
A number can be chosen any number of times from the array 'ARR'.

Elements in each combination must be in non-decreasing order.

For example:
Let the array 'ARR' be [1, 2, 3] and 'B' = 5. Then all possible valid combinations are-
(1, 1, 1, 1, 1)
(1, 1, 1, 2)
(1, 1, 3)
(1, 2, 2)
(2, 3) """


# Solution


def combinationSum(ARR, B, index=0, result=()):
    if B == 0:
        print(result)  # Print valid combination
        return

    for i in range(index, len(ARR)):  # Start from current index to avoid duplicate sets
        if B - ARR[i] >= 0:
            combinationSum(ARR, B - ARR[i], i, result + (ARR[i],))  # Allow repeated use


# Input
n = int(input())  # Number of elements
ARR = list(map(int, input().split()))  # Input array
B = int(input())  # Target sum

# Sort to maintain order and improve efficiency
ARR.sort()

# Call function
combinationSum(ARR, B)
