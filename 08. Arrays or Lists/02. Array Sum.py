# Problem statement

"""
Given an array of length N, you need to find and print the sum of all elements of the array.
"""

# solution


n = int(input())

arr = list(map(int, input().split()))

Sum = 0

for i in arr:
    Sum += i

print(Sum)
