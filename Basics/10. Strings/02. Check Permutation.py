
# Problem statement

""" For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.

Permutations of each other
Two strings are said to be a permutation of each other when either of the string'scratch_KNN.py characters can be rearranged so that
it becomes identical to the other one.

Example:
str1= "sinrtg"
str2 = "string"

The character of the first string(str1) can be rearranged to form str2 and hence we can say that the given strings are
a permutation of each other. """


# solution


def checkPermutation(str1, str2):
    # If lengths are different, they cannot be permutations of each other
    if len(str1) != len(str2):
        return False

    # Initialize a bit vector to track character frequencies (all bits set to 0 initially)
    bit_vector = 0

    # Iterate through each character in str1
    for i in str1:
        # XOR the corresponding bit based on the character'scratch_KNN.py position in the alphabet
        # ord(i) gives the ASCII value of the character, and ord('a') is subtracted to get its index (0-25)
        bit_vector ^= (1 << (ord(i) - ord("a")))

    # Iterate through each character in str2
    for i in str2:
        # XOR the corresponding bit for str2'scratch_KNN.py characters (toggle the bits)
        bit_vector ^= (1 << (ord(i) - ord("a")))

    # If all bits cancel out, meaning both strings have the same characters with the same frequency, return True
    return bit_vector == 0


# Input a strings from the user
str1 = input()
str2 = input()

# Test the function with an example input
print(checkPermutation(str1, str2))
