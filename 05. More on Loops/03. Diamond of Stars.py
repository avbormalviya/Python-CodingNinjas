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

# taking inout

n = int(input())

# divide pattern into two parts

firstHalf = (n + 1) // 2
seconfHalf = n - firstHalf

i = 1

# loops for create and print pattern

while i <= firstHalf:
    j = 1
    k = 1

    while j <= firstHalf - i:
        print(' ', end='')

        j += 1

    while k <= (i * 2) - 1:
        print('*', end='')

        k += 1

    print()
    i += 1

i = 1

while i <= seconfHalf:
    j = 1
    k = 1

    while j <= i:
        print(' ', end='')

        j += 1

    while k <= (seconfHalf - i) * 2 + 1:
        print('*', end='')

        k += 1

    print()
    i += 1
