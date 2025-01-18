
# Problem statement

""" You are given with an array of integers and an integer K. You have to find and print the count of
all such pairs which have difference K.

Note: Take absolute difference between the elements of the array. """


# Solution


def countPairsWithDifferenceK(arr, k):
    """
    Counts the number of pairs with an absolute difference of k.
    :param arr: List[int] - The array of integers
    :param k: int - The absolute difference to check
    :return: int - The count of such pairs
    """
    freq = {}
    count = 0

    # Build frequency map
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Count pairs with difference k
    for num in freq:
        if k == 0:
            # Special case: pairs (num, num)
            count += (freq[num] * (freq[num] - 1)) // 2
        else:
            # Count pairs with num + k and num - k
            if num + k in freq:
                count += freq[num] * freq[num + k]
            if num - k in freq:
                count += freq[num] * freq[num - k]

            # Avoid double counting: remove one direction
            freq[num] = 0

    return count


# Input
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# Output
print(countPairsWithDifferenceK(arr, k))
