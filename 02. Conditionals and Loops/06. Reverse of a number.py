# Problem statement

""" Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be
401 instead of 00401. """

# solution

# taking input

num = int(input())

reverse = 0

# reversing given number num

while num != 0:
    reverse = reverse * 10 + num % 10
    num //= 10

# print reverse of num

print(reverse)
