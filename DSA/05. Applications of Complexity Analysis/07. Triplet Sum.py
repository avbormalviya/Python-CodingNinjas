
# Problem statement

""" You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(scratch_KNN.py) in the
array/list which sum to X.

Note :
Given array/list can contain duplicate elements. """


# solution


def tripletSum(arr, num):
    # Step 1: Sort the array to apply the two-pointer technique effectively
    arr.sort()
    count = 0  # Initialize a counter for the number of triplets

    # Step 2: Iterate through the array, fixing one element at a time
    for i in range(len(arr) - 2):
        # Initialize two pointers:
        j = i + 1  # Pointer to the next element
        k = len(arr) - 1  # Pointer to the last element

        # Step 3: Use two-pointer technique to find pairs that sum to (num - arr[i])
        while j < k:
            current_sum = arr[i] + arr[j] + arr[k]  # Calculate the sum of the triplet

            if current_sum == num:
                count += 1  # Triplet found, increment the count
                j += 1  # Move the left pointer forward
                k -= 1  # Move the right pointer backward
            elif current_sum < num:
                j += 1  # If the sum is too small, move the left pointer forward
            else:
                k -= 1  # If the sum is too large, move the right pointer backward

    # Step 4: Return the total count of triplets found
    return count


# Taking input
n = int(input())  # Number of elements in the array
arr = list(map(int, input().split()))  # Input array of integers
target = int(input())  # Target sum

# Calling the function and printing the result
print(tripletSum(arr, target))

