# Problem statement

""" Write a program to input an integer 'n' and print the sum of all its even digits and the sum of all its odd digits
separately.

Digits mean numbers, not places! That is, if the given integer is "132456", even digits are 2, 4, and 6, and odd digits
are 1, 3, and 5. """

# solution

# taking input n as num

num = int(input())

even = 0
odd = 0

# calculate sum of even and odd numbers

while num != 0:
    if (num % 10) % 2 == 0:
        even += num % 10
    else:
        odd += num % 10

    num //= 10

# print sum of even and odd numbers

print(even, " ", odd)
