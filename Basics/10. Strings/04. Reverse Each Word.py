
# Problem statement

""" Aadil has been provided with a sentence in the form of a string as a function parameter. The task is to implement a
function so as to change the sentence such that each word in the sentence is reversed. A word is a combination of
characters without any spaces.

Example:
Input Sentence: "Hello I am Aadil"
The expected output will look, "olleH I ma lidaA". """


# solution


def reverseEachWords(str):
    # Initialize an empty stack to store characters of the current word
    stuck = []

    # Initialize an empty list to accumulate the result (reversed words)
    result = []

    # Iterate through each character in the input string
    for i in str:
        # If a space is encountered, reverse the current word
        if i == ' ':
            # Pop characters from the stack and append them to result (to reverse the word)
            while stuck:
                result.append(stuck.pop())

            # Add the space to the result to separate the words
            result.append(' ')
        else:
            # If the character is not a space, push it onto the stack
            stuck.append(i)

    # After the loop, there might be one last word to reverse (if the string doesn't end with a space)
    while stuck:
        result.append(stuck.pop())

    # Join the list of characters into a final string and return the result
    return ''.join(result)


# Input a string from the user
str = input()

# Test the function with the user's input
print(reverseEachWords(str))
