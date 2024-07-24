# Problem statement

""" Print the following pattern for the given number of rows.

Assume N is always odd.

Note : There is space after every star. Pattern for N = 7

*
 * *
   * * *
     * * * *
   * * *
 * *
*

"""

# solution

# taking input

n = int(input())

firstHalf = (n + 1) // 2
secondHalf = n - firstHalf

i = 1

# loop for create and print pattern

while i <= firstHalf:
    j = i - 1
    k = 1

    while j >= 1:
        print(' ', end='')

        j -= 1

    while k <= i:
        print('* ', end='')

        k += 1

    print()
    i += 1


i = 1

while i <= secondHalf:
    j = 1
    k = 1

    while j <= secondHalf - i:
        print(' ', end='')

        j += 1

    while k <= secondHalf - i + 1:
        print('* ', end='')

        k += 1

    print()
    i += 1
