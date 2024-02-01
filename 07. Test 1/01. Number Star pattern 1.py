# Problem statement

""" Print the following pattern for given number of rows.

for N = 5:

5432*
543*1
54*21
5*321
*4321

"""

# solution

n = int(input())

i = 1
pos = n

while i <= n:
    j = 1

    while j <= n:
        if j == pos:
            print('*', end='')
        else:
            print(n - j + 1, end='')

        j += 1

    print()

    pos -= 1
    i += 1
