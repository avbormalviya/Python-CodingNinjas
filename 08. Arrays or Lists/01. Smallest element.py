# Problem statement

""" Write a program that returns minimum element in an array.

Hint : the Math.min method is used to find the minimum of two numbers. """


# solution

def minimum_element(arr, n):
    minNum = arr[n - 1]
    for i in arr:
        minNum = min(minNum, i)

    return minNum


n = int(input())
arr = list(map(int, input().split()))
print(minimum_element(arr, n))
