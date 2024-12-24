
# Problem statement

""" Given a string S (that can contain multiple words), you need to find the word which has minimum length.

Note : If multiple words are of same length, then answer will be first minimum length word in the string. Words are
separated by single space only. """


# solution


def minimumLengthWord(string):
    # Initialize variables to store the minimum word length and the word itself
    min_length = float('inf')
    min_word = ""
    current_word = []

    for char in string:
        if char == ' ':  # Word boundary
            # Check and update minimum word if current_word is smaller
            if current_word and len(current_word) < min_length:
                min_length = len(current_word)
                min_word = ''.join(current_word)
            current_word = []  # Reset current word
        else:
            # Add character to current word
            current_word.append(char)

    # Check the last word after the loop ends
    if current_word and len(current_word) < min_length:
        min_word = ''.join(current_word)

    return min_word


# Input from the user
string = input()

# Output the shortest word
print(minimumLengthWord(string))

