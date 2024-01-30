# Problem statement

""" Print the following pattern for the given N number of rows.

Pattern for N = 4

1
11
121
1221

"""

# solution

# taking input

n = int(input())

i = 1

# print to create pattern

while i <= n:
    j = 1

    while j <= i:
        if j == 1 or j == i:
            print(1, end='')
        else:
            print(2, end='')

        j += 1

    print()
    i += 1