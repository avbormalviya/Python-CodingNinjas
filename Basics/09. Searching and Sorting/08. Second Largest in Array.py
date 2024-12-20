
# Problem statement

""" You have been given a random integer array/list(ARR) of size N. You are required to find and return the second
largest element present in the array/list.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 10^2
1<=arr[i]<=10^3

Time Limit: 1 sec """


# solution


def secondLargestInArray(arr):
    # If the array has fewer than two elements, there's no second largest element
    if len(arr) < 2:
        return None  # Return None if there are less than two elements

    # Initialize variables to track the largest and second largest values
    largest = -float('inf')
    second_largest = -float('inf')

    # Iterate over the array to find the largest and second largest values
    for i in arr:
        # If current element is greater than the largest, update both largest and second largest
        if i > largest:
            second_largest = largest  # Update second largest to be the previous largest
            largest = i  # Update largest to the current element
        # If current element is greater than second largest and not equal to the largest, update second largest
        elif i > second_largest and i != largest:
            second_largest = i  # Update second largest

    # If second_largest is still -inf, it means no second largest was found, return None
    return second_largest if second_largest != -float('inf') else None


# Input Handling
n = int(input())  # Read the size of the array
arr = [int(input()) for i in range(n)]  # Read the elements of the array

# Output the result
print(secondLargestInArray(arr))
