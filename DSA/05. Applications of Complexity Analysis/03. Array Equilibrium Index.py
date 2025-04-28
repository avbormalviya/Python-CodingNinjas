
# Problem statement

""" For a given array/list(ARR) of size 'N,' find and return the 'Equilibrium Index' of the array/list.

Equilibrium Index of an array/list is an index 'i' such that the sum of elements at indices [0 to (i - 1)] is equal
to the sum of elements at indices [(i + 1) to (N-1)]. One thing to note here is, the item at the index 'i' is not
included in either part.

If more than one equilibrium indices are present, then the index appearing first in left to right fashion should be
returned. Negative one(-1) if no such index is present.

Example:
Let'scratch_KNN.py consider an array/list Arr = [2, 3, 10, -10, 4, 2, 9]  of size, N = 7.

There exist three equilibrium indices, one at 2, another at 3, and another at 5.

At index 2, the sum of all the elements to the left, [2 + 3] is 5, and the elements to its right, [-10 + 4 + 2 + 9]
is also 5. Hence index 2 is an equilibrium index according to the condition we want to achieve. Mind it that we
haven't included the item at index 2, which is 10, to either of the parts.

Similarly, we can see at index 3 and 5, the elements to its left sum up to 15 and 9 respectively and to the right,
sum up to 15 and 9 respectively either.

Hence the answer would be 2.  """


# solution


def findEquilibriumIndex(arr, n):
    # Calculate the total sum of the array
    total_sum = sum(arr)

    # Initialize left_sum to 0 (sum of elements to the left of the current index)
    left_sum = 0

    # Loop through the array
    for i in range(n):
        # Subtract the current element from total_sum to get the right sum
        total_sum -= arr[i]

        # If left_sum equals the remaining total_sum (right sum), we found the equilibrium index
        if left_sum == total_sum:
            return i

        # Update left_sum by adding the current element
        left_sum += arr[i]

    # If no equilibrium index is found, return -1
    return -1


# Input: size of the array (n)
n = int(input())

# Read the array
arr = list(map(int, input().split()))

# Output: Print the Equilibrium Index
print(findEquilibriumIndex(arr, n))
