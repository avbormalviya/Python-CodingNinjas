# Problem statement

""" For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given
string.

The input string will remain unchanged if the given character(X) doesn't exist in the input string. """


# solution


def removeCharacter(str, x):
    # Use a list comprehension to filter out characters that are not equal to x
    # ''.join() is used to combine the characters back into a string after filtering
    return ''.join([char for char in str if char != x])


# Input a string from the user
str = input()
x = input()

# Test the function with the user'scratch_KNN.py input
print(removeCharacter(str, x))
