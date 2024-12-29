
# Problem statement

""" You are given the starting 'l' and the ending 'r' positions of the array 'ARR'.
You must sort the elements between 'l' and 'r'.

Note:
Change in the input array itself. So no need to return or print anything. """


# solution


# Function to merge two sorted arrays
def mergeTwoSortedArray(arr1, arr2):
    i, j = 0, 0  # Pointers for arr1 and arr2
    result = []  # List to store the merged result

    # Merge the two arrays by comparing elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Append any remaining elements from arr1
    for i in range(i, len(arr1)):
        result.append(arr1[i])

    # Append any remaining elements from arr2
    for j in range(j, len(arr2)):
        result.append(arr2[j])

    return result  # Return the merged array


# Recursive function to perform merge sort
def mergeSort(arr, l, r):
    # Base case: if the array has only one element, return it
    if l == r:
        return [arr[l]]

    # Calculate the middle index
    mid = (l + r) // 2

    # Recursively sort the left and right halves
    left_arr = mergeSort(arr, l, mid)
    right_arr = mergeSort(arr, mid + 1, r)

    # Merge the sorted halves
    return mergeTwoSortedArray(left_arr, right_arr)


# Input: Read array size and elements
n = int(input())
arr = list(map(int, input().split()))

# Output: Print the sorted array using merge sort
print(mergeSort(arr, 0, n - 1))
