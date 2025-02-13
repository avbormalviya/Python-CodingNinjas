
# Problem statement

""" Given a string, find and print all the possible permutations of the input string.

Note :
The order of permutations are not important. Just print them in different lines. """


# Solution


def permutations(arr, left, right):
    """
    Prints all permutations of the given list (arr[left:right+1]) by swapping elements in-place.

    Parameters:
    - arr (List[str]): List representation of the string.
    - left (int): Starting index.
    - right (int): Ending index.
    """

    # Base case: If left index reaches right, print the permutation
    if left == right:
        print("".join(arr))
        return

    for i in range(left, right + 1):
        # Swap the current character to the left position
        arr[left], arr[i] = arr[i], arr[left]

        # Recur with the next index
        permutations(arr, left + 1, right)

        # Backtrack: Undo the swap to restore original order
        arr[left], arr[i] = arr[i], arr[left]


# Input handling
string = input().strip()
arr = list(string)  # Convert string to a list for in-place swapping

# Generate and print all permutations
permutations(arr, 0, len(arr) - 1)
