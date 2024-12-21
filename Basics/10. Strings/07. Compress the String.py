
# Problem statement

""" Write a program to do basic string compression. For a character which is consecutively repeated more than once,
replace consecutive duplicate occurrences with the count of repetitions.

Example:
If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".
The string is compressed only when the repeated character count is more than 1.

Note:
Consecutive count of every character in the input string is less than or equal to 9. You are not required to print
anything. It has already been taken care of. Just implement the given function and return the compressed string. """


# solution


def compressTheString(string):
    # Initialize an empty list to store the result
    result = []

    # Initialize count to 1 since we are starting with the first character
    count = 1

    # Set the current character to the first character in the string
    curr = string[0]

    # Iterate through the string starting from the second character
    for i in range(1, len(string)):
        # If the current character is the same as the previous one, increase the count
        if string[i] == curr:
            count += 1
        else:
            # If the character changes, append the previous character to the result
            result.append(curr)

            # If the character appeared more than once, append the count
            if count > 1:
                result.append(str(count))

            # Update the current character to the new one and reset the count
            curr = string[i]
            count = 1

    # Append the last character to the result
    result.append(curr)

    # If the last character appeared more than once, append the count
    if count > 1:
        result.append(str(count))

    # Join the list into a string and return the compressed result
    return ''.join(result)


# Input a string from the user
string = input()

# Test the function with the user's input
print(compressTheString(string))
