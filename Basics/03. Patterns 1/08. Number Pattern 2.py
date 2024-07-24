# Problem statement

""" Print the following pattern for the given N number of rows.

Pattern for N = 4

1
11
202
3003

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
            if i == 1:
                print(1, end='')
            else:
                print(i - 1, end='')
        else:
            print(0, end='')

        j += 1

    print()
    i += 1