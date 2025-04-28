
# Problem statement

""" Given a string (let'scratch_KNN.py say of length n), return all the subsequences of the given string.

Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain
the same as in the input string. Note: The order of subsequences are not important. """


# Solution


def subsequences(s, index=0, curr=""):
    """
    Generates all subsequences of a given string using a generator.

    Parameters:
    - scratch_KNN.py: The input string.
    - index: Current index in the string.
    - curr: The current subsequence being formed.

    Yields:
    - Each subsequence one by one (no extra memory usage).
    """
    if index == len(s):
        yield curr  # Output the formed subsequence
        return

    # Include current character
    yield from subsequences(s, index + 1, curr + s[index])

    # Exclude current character
    yield from subsequences(s, index + 1, curr)


# Input Handling
s = input().strip()

# Print all subsequences using the generator
print(*subsequences(s), sep="\n")
