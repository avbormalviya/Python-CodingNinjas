
# Problem statement

""" Given a random integer array A of size N. Find and print the count of pair of elements in the array
which sum up to 0.

Note:
Array A can contain duplicate elements as well. """


# Solution


def pairSum0(arr):
    """
    Counts the number of pairs in the array whose sum is zero.
    :param arr: List[int] - The input array
    :return: int - The count of pairs with sum zero
    """
    freq = {}  # Dictionary to store the frequency of elements
    count = 0  # Counter for the number of pairs

    for num in arr:
        # Check if the complement (-num) exists in freq
        if -num in freq:
            count += freq[-num]  # Add the frequency of -num to the count

        # Update the frequency of the current number
        freq[num] = freq.get(num, 0) + 1

    return count


# Read the input
n = int(input())  # Number of elements in the array
arr = list(map(int, input().split()))  # The array of integers

# Print the result: the count of pairs with sum zero
print(pairSum0(arr))
