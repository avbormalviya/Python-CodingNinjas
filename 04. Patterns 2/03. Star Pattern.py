# Problem statement

""" Print the following pattern

Pattern for N = 4

...*
..***
.*****
*******

Hint

As taught in the video, you just have to modify the code so that instead of printing numbers,
it should output stars ('*').

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
        print('*', end='')

        k += 1

    while l >= 1:
        print('*', end='')

        l -= 1

    print()
    i += 1
