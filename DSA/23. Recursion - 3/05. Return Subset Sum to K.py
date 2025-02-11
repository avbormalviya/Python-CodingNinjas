
# Problem statement

""" Given an array A of size n and an integer K, return all subsets of A which sum to K.

Subsets are of length varying from 0 to n, that contain elements of the array. But the order of
elements should remain same as in the input array.

Note :
The order of subsets are not important. """


def subsetsSumK(a, n, k, curr=None, result=None):
    if curr is None:
        curr = []
    if result is None:
        result = []

    if n == 0:
        if k == 0:
            result.append(list(curr))  # Store a copy of the subset
        return  # Instead of returning result, just return from this call

    # Include the current element
    curr.append(a[n - 1])
    subsetsSumK(a, n - 1, k - a[n - 1], curr, result)

    # Backtrack: Remove the element and explore other possibilities
    curr.pop()
    subsetsSumK(a, n - 1, k, curr, result)

    return result  # Return only at the end of the function


# Input Handling
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# Find and print subsets
print(*subsetsSumK(arr, n, k), sep="\n")
