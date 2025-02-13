
# Problem statement

""" Given an array A and an integer K, print all subsets of A which sum to K.

Subsets are of length varying from 0 to n, that contain elements of the array.
But the order of elements should remain same as in the input array.

Note :
The order of subsets are not important. Just print them in different lines. """


# Solution


def printSubsetSumK(arr, n, k, output=None):
    """
    Prints all subsets of `arr` that sum up to `k`.

    Parameters:
    - arr (List[int]): Input list of numbers
    - n (int): Current index being considered
    - k (int): Target sum
    - output (List[int]): Current subset being formed
    """

    # Initialize output list for the first call
    if output is None:
        output = []

    # Base case: If sum becomes 0, print the subset
    if k == 0:
        print(output)
        return

    # If no more elements left or k < 0, stop recursion
    if n == 0 or k < 0:
        return

    # Include current element and recur
    output.append(arr[n - 1])
    printSubsetSumK(arr, n - 1, k - arr[n - 1], output)

    # Exclude current element and recur (backtrack)
    output.pop()
    printSubsetSumK(arr, n - 1, k, output)


# Input handling
n = int(input().strip())
arr = list(map(int, input().split()))
k = int(input().strip())

# Find and print subsets that sum to k
printSubsetSumK(arr, n, k)
