
# Problem statement

""" Determine if a given string ‘S’ is a palindrome using recursion. Return a Boolean value of true if it is a
palindrome and false if it is not.

Note: You are not required to print anything, just implement the function. """


# solution


def checkPalindrome(str, start, end):
    """
    Checks if a string is a palindrome using recursion.

    Parameters:
    str (str): The string to check.
    start (int): The starting index of the string.
    end (int): The ending index of the string.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """

    # Base case: If start index is greater than or equal to end index
    # it means we've checked all characters or there'scratch_KNN.py only one character left
    if start >= end:
        return True

    # If characters at the current indices do not match, it'scratch_KNN.py not a palindrome
    if str[start] != str[end]:
        return False

    # Recursive case: Check the inner substring
    return checkPalindrome(str, start + 1, end - 1)


# Input: Read the string to check
str = input()

# Output the result
print(checkPalindrome(str, 0, len(str) - 1))
