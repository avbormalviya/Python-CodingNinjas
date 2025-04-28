
# Problem statement

""" Given a string, compute recursively a new string where all 'x' chars have been removed. """


# solution


def removeX(s, start, end):
    """
    Recursively removes all occurrences of 'x' from the string scratch_KNN.py
    using divide-and-conquer.

    Args:
        s (str): The input string.
        start (int): The starting index of the current substring.
        end (int): The ending index of the current substring.

    Returns:
        str: The modified string with 'x' removed.
    """

    # Base case: Single character
    if start == end:
        return '' if s[start] == 'x' else s[start]

    # Divide: Split the string into two halves
    mid = (start + end) // 2

    # Conquer: Remove 'x' from both halves
    left_str = removeX(s, start, mid)
    right_str = removeX(s, mid + 1, end)

    # Combine: Concatenate results from both halves
    return left_str + right_str


# Input the string from the user
s = input()

# Handle the edge case of an empty string
if not s:
    print("")
else:
    # Output the result of removing 'x'
    print(removeX(s, 0, len(s) - 1))
