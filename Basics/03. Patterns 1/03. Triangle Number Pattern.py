# Problem statement

""" Print the following pattern for the given N number of rows.

Pattern for N = 4

1
22
333
4444

"""

# solution

# taking input

n = int(input())

i = 1

# print to create pattern

while i <= n:
    j = 1

    while j <= i:
        print(i, end='')

        j += 1

    print()
    i += 1

