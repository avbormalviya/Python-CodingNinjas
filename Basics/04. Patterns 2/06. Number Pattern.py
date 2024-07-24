# Problem statement

""" Print the following pattern for n number of rows.

Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n.
You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1

For eg. N = 5

1........1
12......21
123....321
1234..4321
1234554321

"""

# solution

# taking input

n = int(input())

i = 1

# print to create pattern

while i <= n:
    j = 1
    k = 1
    l = 1

    while j <= i:
        print(j, end='')

        j += 1

    while k <= (n - i) * 2:
        print(' ', end='')

        k += 1

    while l <= i:
        print(i - l + 1, end='')

        l += 1

    print()
    i += 1
