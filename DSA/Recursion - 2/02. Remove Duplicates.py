
# Problem statement

""" Given a string S, remove consecutive duplicates from it recursively. """


# solution


def removeDuplicates(str, start, end):
    """
    Removes adjacent duplicates from the string recursively.

    Args:
        str (str): The input string.
        start (int): The starting index of the current substring.
        end (int): The ending index of the current substring.

    Returns:
        str: The modified string with adjacent duplicates removed.
    """
    # Base case: Single character, no duplicates to remove
    if start == end:
        return str[start]

    # Divide: Split the string into two halves
    mid = (start + end) // 2

    # Recursively process the left and right halves
    left_str = removeDuplicates(str, start, mid)
    right_str = removeDuplicates(str, mid + 1, end)

    # Handle the case where duplicates are present between left and right halves
    if left_str[-1] == right_str[0]:
        return left_str + right_str[1:]

    return left_str + right_str


def removeAdjacentDuplicates(s):
    """
    Wrapper function to start recursion on the full string.
    """
    # Handle edge case for empty string
    if not s:
        return s

    # Start recursion for the entire string
    return removeDuplicates(s, 0, len(s) - 1)


# Input the string from the user
s = input()

# Output the result of removing adjacent duplicates
print(removeAdjacentDuplicates(s))
