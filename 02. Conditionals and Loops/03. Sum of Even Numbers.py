# Problem statement

# Given a number N, print sum of all even numbers from 1 to N.

# solution

# taking input

n = int(input())

count = 2
sum = 0

# calculate sum of all even numbers from 1 to N.

while count <= n:
    sum += count
    count += 2

# print sum.

print(sum)