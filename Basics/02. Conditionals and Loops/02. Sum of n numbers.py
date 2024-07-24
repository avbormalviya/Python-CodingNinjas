# Problem statement

""" Given an integer n, find and print the sum of numbers from 1 to n.

Note - Use while loop only. """

# solution

# taking input

n = int(input())

count = 1
sum = 0

# find the sum of numbers from 1 to n.

while count <= n:
    sum += count
    count += 1
    
# print the sum.

print(sum)
