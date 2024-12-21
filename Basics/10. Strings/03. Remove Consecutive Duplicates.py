
# Problem statement

""" For a given string(str), remove all the consecutive duplicate characters.

Example:
Input String: "aaaa"
Expected Output: "a"

Input String: "aabbbcc"
Expected Output: "abc"

Input Format:
The first and only line of input contains a string without any leading and trailing spaces. All the characters in the
string would be in lower case.

Output Format:
The only line of output prints the updated string.

Note:
You are not required to print anything. It has already been taken care of. """


# solution


def removeConsecutiveDuplicates(str):
    # Initialize an empty string to track the previous character
    curr = ""

    # Initialize an empty string to build the result without consecutive duplicates
    result = ""

    # Iterate through each character in the input string 'str'
    for i in str:
        # If the current character is not the same as the previous one
        if (i != curr):
            # Add the current character to the result string
            result += i
            # Update 'curr' to be the current character
            curr = i

    # Return the result string with no consecutive duplicates
    return result


# Input a strings from the user
str = input()

# Test the function with an example input
print(removeConsecutiveDuplicates(str))
