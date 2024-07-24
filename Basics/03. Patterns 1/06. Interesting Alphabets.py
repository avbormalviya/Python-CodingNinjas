# Problem statement

""" Print the following pattern for the given number of rows.

Pattern for N = 5

E
DE
CDE
BCDE
ABCDE

"""

# solution

# taking input

n = int(input())

i = 1

# print to create patten

while i <= n:
    j = 1

    while j <= i:
        print(chr(n - i + j + 64), end='')

        j += 1

    print()
    i += 1

