# Problem statement

""" You are given an integer array 'A' of size 'N', sorted in non-decreasing order. You are also given an integer 'target'. Your task is to write a function to search for 'target' in the array 'A'. If it exists, return its index in 0-based indexing. If 'target' is not present in the array 'A', return -1.

Note:
You must write an algorithm whose time complexity is O(LogN) """


# solution


def search(nums: [int], target: int):
    # Initialize the low and high pointers for the search range
    low = 0
    high = len(nums) - 1

    # Start the binary search loop
    while low <= high:
        # Calculate the midpoint of the current range
        mid = (low + high) // 2  # Corrected mid calculation

        # If the element at mid is the target, return the index
        if nums[mid] == target:
            return mid
        # If the target is smaller, discard the right half
        elif nums[mid] > target:
            high = mid - 1
        # If the target is larger, discard the left half
        else:
            low = mid + 1

    # If the target is not found, return -1
    return -1


# Read the number of elements in the array
n = int(input())
numbers = list()

# Take input for each element and store it in the numbers list
for _ in range(n):
    ele = int(input())
    numbers.append(ele)

# Read the target number to search for
target = int(input())

# Call the search function and print the result
print(search(numbers, target))
