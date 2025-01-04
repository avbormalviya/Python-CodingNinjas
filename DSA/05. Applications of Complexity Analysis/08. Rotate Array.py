
# Problem statement

""" You have been given a random integer array/list(ARR) of size N. Write a function that rotates the given array/list
by D elements(towards the left).

Note:
Change in the input array/list itself.You don't need to return or print the elements. """


# solution


def rotateArraySlice(arr, s, e):
    """
    Reverses a section of the array between indices s and e (inclusive).
    """
    while s < e:
        # Swap the elements at indices s and e
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1
    return arr  # Return the modified array


def rotateArray(arr, n, d):
    """
    Rotates the array `arr` of size `n` to the left by `d` positions.
    """
    # Step 1: Reverse the first `d` elements
    rotateArraySlice(arr, 0, d - 1)

    # Step 2: Reverse the remaining `n - d` elements
    rotateArraySlice(arr, d, n - 1)

    # Step 3: Reverse the entire array to achieve the final rotation
    rotateArraySlice(arr, 0, n - 1)

    return arr  # Return the rotated array


# Taking input
n = int(input())  # Number of elements in the array
arr = list(map(int, input().split()))  # Input array of integers
target = int(input())  # Target sum

# Calling the function and printing the result
print(rotateArray(arr, n, target))
