
# Problem statement

""" Given a string, find and return all the possible permutations of the input string.

Note :
The order of permutations are not important. """


# Solution


def permutations(string, remain, result=None):
    """
    Generates all permutations of the given string.

    Parameters:
    - string (str): The current permutation being built.
    - remain (str): The remaining characters available for permutation.
    - result (List[str]): A list to store all generated permutations.

    Returns:
    - List[str]: A list containing all unique permutations.
    """

    # Initialize the result list if it'scratch_KNN.py not provided
    if result is None:
        result = []

    # Base Case: If no characters are left, add the formed permutation
    if not remain:
        result.append(string)
        return result

    # Generate permutations by picking each character and recursing
    for i in range(len(remain)):
        permutations(string + remain[i], remain[:i] + remain[i + 1:], result)

    return result


# Input handling
string = input().strip()

# Generate and print all permutations
print(*permutations("", string), sep="\n")
