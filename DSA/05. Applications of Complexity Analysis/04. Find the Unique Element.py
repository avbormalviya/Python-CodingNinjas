
# Problem statement

""" You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].

Now, in the given array/list, 'M' numbers are present twice and one number is present only once.

You need to find and return that number which is unique in the array/list.

Note:
Unique element is always present in the array/list according to the given condition. """


# solution


def findUniqueElement(arr):
    result = 0

    # XOR all the elements of the array
    for num in arr:
        result ^= num

    # The result will hold the unique element
    return result


# Input: size of the array (n)
n = int(input())

# Read the array
arr = list(map(int, input().split()))

# Output: Print the Unique Element
print(findUniqueElement(arr))
