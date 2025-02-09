
# Problem statement

""" You are given an array “arr'' of integers. Your task is to find the contiguous subarray within the array which has the largest product of its elements. You have to report this maximum product.

An array c is a subarray of array d if c can be obtained from d by deletion of several elements from the beginning and several elements from the end.

For e.g.- The non-empty subarrays of an array [1,2,3] will be- [1],[2],[3],[1,2],[2,3],[1,2,3].
For Example:
If arr = {-3,4,5}.
All the possible non-empty contiguous subarrays of “arr” are {-3}, {4}, {5}, {-3,4}, {4,5} and {-3,4,5}.
The product of these subarrays are -3, 4, 5, -12, 20 and -60 respectively.
The maximum product is 20. Hence, the answer is 20.
Follow Up:
Can you solve this in linear time and constant space complexity? """


# Solution


def maxProduct(arr, n):
    """
    Function to find the maximum product subarray.

    Parameters:
    - arr: List of integers.
    - n: Size of the array.

    Returns:
    - Maximum product of a contiguous subarray.
    """
    # Initialize max and min products to the first element
    max_so_far = arr[0]
    min_so_far = arr[0]
    result = arr[0]

    # Start loop from the second element (index 1)
    for i in range(1, n):
        curr = arr[i]

        # Store previous max_so_far before updating min_so_far
        temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        # Update max_so_far after min_so_far is updated
        max_so_far = temp_max

        # Update final result
        result = max(result, max_so_far)

    return result


# 🟢 Input Handling
n = int(input())  # Number of elements
arr = list(map(int, input().split()))  # Read array

# 🟢 Solve the problem
print(maxProduct(arr, n))

