
# Problem statement

""" You are given an array of integers that contain numbers in random order. Write a program to find and return
the number which occurs the maximum times in the given input.

If two or more elements are having the maximum frequency, return the element which occurs in the array first. """


# Solution


from collections import Counter


def maxFrequency(arr):
    """
    Finds the element with the highest frequency in the array.
    In case of a tie, returns the smallest element among those with the highest frequency.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        int: The element with the highest frequency.
    """
    if not arr:
        return None

    # Count the frequencies
    freq = Counter(arr)

    # Find the maximum frequency
    max_freq = max(freq.values())

    # Find the smallest element with the maximum frequency
    return min(key for key, count in freq.items() if count == max_freq)


# Read the input
n = int(input())

# Read the array
arr = list(map(int, input().split()))

# Print the result
print(maxFrequency(arr))
