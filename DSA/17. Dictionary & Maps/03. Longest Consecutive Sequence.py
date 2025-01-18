
# Problem statement

""" You are given an unsorted array/list 'ARR' of 'N' integers. Your task is to return the length of the longest
consecutive sequence.

The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2, ..., 'NUM' + L] where 'NUM' is the starting
integer of the sequence and 'L' + 1 is the length of the sequence.

Note:
If there are any duplicates in the given array we will count only one of them in the consecutive sequence.

For example-
For the given 'ARR' [9,5,4,9,10,10,6].

Output = 3
The longest consecutive sequence is [4,5,6].

Follow Up:
Can you solve this in O(N) time and O(N) space complexity? """


# Solution


def longestConsecutiveSequence(arr):
    # Convert the list into a set for O(1) average-time complexity for lookups
    numSet = set(arr)

    # Variable to store the length of the longest consecutive sequence found
    maxLen = 0

    # Iterate through each number in the array
    for num in arr:
        # If num-1 is not in the set, then num is the start of a potential sequence
        if num - 1 not in numSet:
            currNum = num  # Start of the sequence
            currLen = 1  # Length of the current sequence

            # While the next number (currNum + 1) is in the set, keep extending the sequence
            while currNum + 1 in numSet:
                currNum += 1  # Move to the next number in the sequence
                currLen += 1  # Increase the length of the current sequence

            # Update maxLen if the current sequence is the longest so far
            maxLen = max(maxLen, currLen)

    # Return the length of the longest consecutive sequence
    return maxLen


# Read the input
n = int(input())  # Read the number of elements (though we don’t really need to use it here)
arr = list(map(int, input().split()))  # Read the array as a list of integers

# Print the result: the length of the longest consecutive sequence
print(longestConsecutiveSequence(arr))
