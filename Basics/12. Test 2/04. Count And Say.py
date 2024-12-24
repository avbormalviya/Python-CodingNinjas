
# Problem statement

""" Write as you speak is a special sequence of strings that starts with string “1” and after one iteration you rewrite
the sequence as whatever you speak.

Example :
The first few iterations of the sequence are :

First iteration: “1”
    As we are starting with one.

Second iteration: “11”
    We speak “1” as   “one 1” then we write it as “11”

Third iteration: “21”
    We speak “11” as “Two 1” then we write it as “21”

Fourth iteration: “1211”
    We speak “21” as “one 2, one 1”  then we write it as “1211”

Fifth iteration: “111221”
    We speak “1211” as “one 1, one 2, two 1” then we write it as “111221”

Sixth iteration: “312211”
    We speak “111221” as “three 1, two 2, one 1” then we write it as “312211”

You will be given a single positive integer N, Your task is to write the sequence after N iterations. """


# solution


def countAndSay(n):
    # Base case: First sequence
    say = '1'

    for _ in range(n):
        current = say[0]
        count = 1
        new_say = []

        # Iterate through the string starting from the second character
        for char in say[1:]:
            if char == current:
                count += 1
            else:
                # Append count and current character to the new sequence
                new_say.append(str(count))
                new_say.append(current)
                current = char
                count = 1

        # Append the last group
        new_say.append(str(count))
        new_say.append(current)

        # Update say with the new sequence
        say = ''.join(new_say)

    return say


# Taking Input
n = int(input())

# Print the Result
print(countAndSay(n))
