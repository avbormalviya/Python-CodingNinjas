# Problem statement

""" Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member
of fibonacci series else false.

Note:
Fibonacci series is the series of numbers where each number is obtained by adding two previous numbers.
The first two numbers in the Fibonacci series are 0 and 1. """


# solution

def checkMember(n):
    first = 0
    second = 1
    ans = 0
    while True:
        if ans == n:
            return True
        elif ans > n:
            return False

        ans = first + second
        first = second
        second = ans


n = int(input())
if checkMember(n):
    print("true")
else:
    print("false")
