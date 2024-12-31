
# Problem statement

""" Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string
was generated using the following rules:

a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'

If all the rules are followed by the given string, return true otherwise return false """


# solution


def isValidString(s):
    # Base case: empty string is valid
    if len(s) == 0:
        return True

    # If the string starts with 'a'
    if s[0] == 'a':
        # Case 1: Single 'a', recurse on the rest
        if len(s) == 1:
            return True
        # Case 2: 'a' followed by another 'a'
        elif s[1] == 'a':
            return isValidString(s[1:])
        # Case 3: 'a' followed by 'bb'
        elif len(s) > 2 and s[1:3] == "bb":
            return isValidString(s[3:])
        else:
            return False

    # If the string starts with anything other than 'a'
    return False


# Input: The string to validate
s = input()

# Output: Check if the string is valid
print(isValidString(s))
