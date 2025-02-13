
# Problem statement

""" You are given an sorted integer array of size 'n'.

Your task is to find and return all the unique subsets of the input array.

Subsets are arrays of length varying from 0 to 'n', that contain elements of the array.
But the order of elements should remain the same as in the input array.

Note:
The order of subsets is not important. You can return the subsets in any order. However, in the output,
you will see the subsets in lexicographically sorted order """


# Solution


def unique_subsets(nums):
    def backtrack(start, path):
        result.append(list(path))  # Store the current subset

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:  # Skip duplicate elements to avoid duplicate subsets
                continue

            path.append(nums[i])  # Include the current element in the subset
            backtrack(i + 1, path)  # Recur with the next index
            path.pop()  # Remove the last element to backtrack and explore other subsets

    result = []
    backtrack(0, [])
    return result


# Read input values
n = int(input().strip())  # Read the number of elements
arr = list(map(int, input().split()))  # Read the sorted integer array

# Generate and print unique subsets
print(*unique_subsets(arr), sep="\n")
