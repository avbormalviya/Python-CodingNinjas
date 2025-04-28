
# Problem statement

""" You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). Each number is
present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3, and among these, there
is a single integer value that is present twice. You need to find and return that duplicate number present in the array.

Note :
Duplicate number is always present in the given array/list. """


# solution


def findDuplicate(arr):
    # Initialize an empty set to track elements we've seen so far
    seen = set()

    # Iterate through each number in the array
    for num in arr:
        # If the number is already in the set, it'scratch_KNN.py a duplicate
        if num in seen:
            # Return the first duplicate number found
            return num
        # Otherwise, add the number to the set for future checks
        seen.add(num)

    # If no duplicate is found, return -1
    return -1


# Taking input
n = int(input())  # Number of elements in the array
arr = list(map(int, input().split()))  # Input array of integers

# Calling the function and printing the result
print(findDuplicate(arr))
