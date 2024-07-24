# Problem statement

""" Write a program to find the Nth Fibonacci number using loops.

Note :

The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually
starting with first_number  and Second_number .
First_number and Second_number in this question will be 1 . Soo that the resultant series
will be 1, 1, 2, 3, 5, 8 ... """

# solution

# taking input integer as num

num = int(input())

pre1 = 0
pre2 = 1
ans = 1

i = 1

# calculate Nth Fibonacci number

while i != num:
    ans = pre1 + pre2
    pre1 = pre2
    pre2 = ans
    i += 1

# print Nth Fibonacci number

print(ans)
