# Problem statement

""" Print the following pattern for a given n.

For eg. N = 6

123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456

"""

# solution

# taking input

n = int(input())

i = 1

# loops for create and print pattern

while i <= n:
    j = i - 1
    k = 1

    while j >= 1:
        print(' ', end='')

        j -= 1

    while k <= n - i + 1:
        print(i + k - 1, end='')

        k += 1

    print()
    i += 1

i = 1

while i <= n - 1:
    j = 1
    k = 1

    while j <= n - i - 1:
        print(' ', end='')

        j += 1

    while k <= i + 1:
        print(n - i + k - 1, end='')

        k += 1

    print()
    i += 1
