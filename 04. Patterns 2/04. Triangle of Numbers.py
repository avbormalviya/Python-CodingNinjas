# Problem statement

""" Print the following pattern for the given number of rows.

Pattern for N = 4

...1
..232
.34543
4567654

The dots represent spaces. """

# solution

# taking input

n = int(input())

i = 1

# print to create pattern

while i <= n:
    j = 1
    k = 1
    l = i - 1

    while j <= n - i:
        print(' ', end='')

        j += 1

    while k <= i:
        print(i + k - 1, end='')

        k += 1

    while l >= 1:
        print(l + i - 1, end='')

        l -= 1

    print()
    i += 1

