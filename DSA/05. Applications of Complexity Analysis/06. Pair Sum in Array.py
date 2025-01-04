
# Problem statement

""" You have been given an integer array/list(ARR) and a number 'num'. Find and return the total number of pairs in
the array/list which sum to 'num'.

Note:
Given array/list can contain duplicate elements.  """


# solution


from collections import Counter


def pairSumInArray(arr, target):
    counter = Counter(arr)
    count = 0

    for val in list(counter):
        complement = target - val

        # Check if the complement exists in the Counter
        if complement in counter:
            if val == complement:
                # Special case: Pair of the same element (e.g., 2 + 2 = 4)
                count += (counter[val] * (counter[val] - 1)) // 2
            else:
                # Count the pairs and remove both values from the Counter
                count += counter[val] * counter[complement]
            del counter[val]
            del counter[complement]

    return count


# Taking input
n = int(input())  # Number of elements in the array
arr = list(map(int, input().split()))  # Input array of integers
target = int(input())  # Target sum

# Calling the function and printing the result
print(pairSumInArray(arr, target))
