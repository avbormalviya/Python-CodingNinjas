
# Problem statement

""" For a given a string(str), find and return the highest occurring character.

Example:
Input String: "abcdeapapqarr"

Expected Output: 'a'

Since 'a' has appeared four times in the string which happens to be the highest frequency character, the answer would
be 'a'. If there are two characters in the input string with the same frequency, return the character which comes first.

Consider:
Assume all the characters in the given string to be in lowercase always. """


# solution


def highestOccurringCharacter(str):
    count_arr = [0 for _ in range(26)]

    for i in str:
        if i == ' ':
            continue

        count_arr[ord(i) - ord('a')] += 1

    return chr(count_arr.index(max(count_arr)) + ord('a'))


# Input a string from the user
str = input()

# Test the function with the user's input
print(highestOccurringCharacter(str))
