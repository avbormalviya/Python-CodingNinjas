
# Problem statement

""" You have been given a random integer array/list(ARR) of size N. You have been required to push all the zeros that
are present in the array/list to the end of it. Also, make sure to maintain the relative order of the non-zero elements.

Note:
Change in the input array/list itself. You don't need to return or print the elements.

You need to do this in one scan of array only. Don't use extra space.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
Time Limit: 1 sec """


# solution


def pushZerosToEnd(arr):
    non_zero_index = 0  # Pointer to place the next non-zero element

    # Traverse the array
    for i in range(len(arr)):
        if arr[i] != 0:  # Check for non-zero elements
            # Swap current element with the element at non_zero_index
            arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
            non_zero_index += 1  # Move pointer forward

    return arr


# Input Handling
n = int(input())
arr = [int(input()) for i in range(n)]

# Output the result
print(pushZerosToEnd(arr))
