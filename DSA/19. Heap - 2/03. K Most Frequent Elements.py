
# Problem statement

""" You are given an Integer array ‘ARR’ and an Integer ‘K’.
Your task is to find the ‘K’ most frequent elements in ‘ARR’. Return the elements in any order.

For Example:
You are given ‘ARR’ = {1, 2, 2, 3, 3} and ‘K’ = 2.
The answer will {2, 3} as 2 and 3 are the elements occurring most times. """


# Solution


def KMostFrequent(n, k, arr):
    """
    Finds the k most frequent elements in the array.

    Parameters:
    n (int): Number of elements in the array.
    k (int): Number of most frequent elements to return.
    arr (list): List of integers.

    Returns:
    list: A list of the k most frequent elements.
    """
    # Step 1: Create a frequency dictionary
    freq_dict = {}
    for i in arr:
        freq_dict[i] = freq_dict.get(i, 0) + 1  # Increment frequency for each element

    # Step 2: Create a bucket to group elements by frequency
    # The bucket index represents the frequency, and each bucket contains elements with that frequency
    bucket = [[] for _ in range(n + 1)]
    for val, freq in freq_dict.items():
        bucket[freq].append(val)

    # Step 3: Collect the k most frequent elements
    ans = []  # Result list to store the k most frequent elements

    # Traverse the bucket from highest frequency to lowest
    for i in range(n, 0, -1):  # Start from the maximum possible frequency
        if not bucket[i]:  # Skip if no elements with the current frequency
            continue

        # Add elements from the current bucket to the result
        for val in bucket[i]:
            ans.append(val)
            k -= 1  # Decrease the count of required elements

            if k == 0:  # Stop once we have collected k elements
                break

        if k == 0:  # Break the outer loop as well
            break

    return ans


# Input: Read the number of elements in the array
n = int(input())

# Input: Read the array elements
arr = list(map(int, input().split()))

# Input: Read the value of k
k = int(input())

# Output: Print the k most frequent elements
print(KMostFrequent(n, k, arr))
