# Problem statement

""" Print the following pattern for the given N number of rows.

Pattern for N = 3

A
BB
CCC

"""

# solution

# taking input

n = int(input())

i = 1

# print to create pattern

while i <= n:
    j = 1

    while j <= i:
        print(chr(i + 64), end='')

        j += 1

    print()
    i += 1