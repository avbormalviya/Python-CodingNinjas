
# Problem statement

""" Given a string, determine if it is a palindrome, considering only alphanumeric characters.

Palindrome
A palindrome is a word, number, phrase, or other sequences of characters which read the same backwards and forwards.

Example:
If the input string happens to be, "malayalam" then as we see that this word can be read the same as forward and
backwards, it is said to be a valid palindrome.

The expected output for this example will print, 'true'.
From that being said, you are required to return a boolean value from the function that has been asked to implement. """


# solution


def stringPalindrome(str):
    # Initialize pointers to the start and end of the string
    start_pointer = 0
    end_pointer = len(str) - 1

    # Loop until the pointers cross each other
    while start_pointer < end_pointer:
        # If characters at the current pointers do not match, it'scratch_KNN.py not a palindrome
        if str[start_pointer] != str[end_pointer]:
            return False

        # Move the pointers closer to the center
        start_pointer += 1
        end_pointer -= 1

    # If the loop completes without returning False, the string is a palindrome
    return True


# Input a string from the user
str = input()

# Check if the string is a palindrome and print the result
print(stringPalindrome(str))

