
# Problem statement

""" Given a string S, you need to remove all the duplicates. That means, the output string should contain each
character only once. The respective order of characters should remain same, as in the input string. """


# Solution


from collections import Counter


def uniqueChars(string):
    """
    Removes all duplicate characters from the given string.
    :param string: str - The input string
    :return: str - The string with only unique characters
    """
    # Count the frequency of each character
    freq = Counter(string)

    # Construct the output string with unique characters
    return "".join(char for char in freq)


# Read the input string
string = input()

# Print the result: the string with only unique characters
print(uniqueChars(string))
