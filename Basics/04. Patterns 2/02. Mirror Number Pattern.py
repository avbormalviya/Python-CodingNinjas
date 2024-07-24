# Problem statement

""" Print the following pattern for the given N number of rows.

Pattern for N = 4

...1
..12
.123
1234

The dots represent spaces.

"""

# solution

# taking input

n = int(input())

i = 1

# print to create pattern

while i <= n:
    j = 1
    k = 1

    while j <= n - i:
        print(' ', end='')

        j += 1

    while k <= i:
        print(k, end='')

        k += 1

    print()
    i += 1