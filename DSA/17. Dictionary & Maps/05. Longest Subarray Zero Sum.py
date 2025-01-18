
# Problem statement

""" Given an array consisting of positive and negative integers, find the length of the longest
subarray whose sum is zero. """


# Solution


def lengthOfLongestSubarray(arr):
    # Dictionary to store the first occurrence of each cumulative sum
    indexMap = {}
    currSum = 0
    maxLen = 0

    for i in range(len(arr)):
        currSum += arr[i]

        # If the cumulative sum is zero, the subarray from the start to i has a zero sum
        if currSum == 0:
            maxLen = i + 1

        # If the cumulative sum is already in the map, calculate the subarray length
        if currSum in indexMap:
            maxLen = max(maxLen, i - indexMap[currSum])
        else:
            # Otherwise, store the first occurrence of this sum
            indexMap[currSum] = i

    return maxLen


# Read the input
n = int(input())  # Number of elements in the array
arr = list(map(int, input().split()))  # Array of integers

# Print the result: the length of the longest subarray with zero sum
print(lengthOfLongestSubarray(arr))
