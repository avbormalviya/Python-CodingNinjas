# Problem statement

""" Print the following pattern for the given number of rows.

Note: N is always odd.

Pattern for N = 5

..*
.***
*****
.***
..*

The dots represent spaces. """

# solution

# taking input

n = int(input())

firstHalf = (n + 1) // 2
secondHalf = n - firstHalf

i = 1

# print to create pattern

while i <= firstHalf:
    j = 1
    k = 1
    l = i - 1

    while j <= firstHalf - i:
        print(' ', end='')

        j += 1

    while k <= i:
        print('*', end='')

        k += 1

    while l >= 1:
        print('*', end='')

        l -= 1

    print()
    i += 1

i = 1

while i <= secondHalf:
    j = 1
    k = 1
    l = 1

    while j <= i:
        print(' ', end='')

        j += 1

    while k <= secondHalf - i:
        print('*', end='')

        k += 1

    while l <= secondHalf - i + 1:
        print('*', end='')

        l += 1

    print()
    i += 1















