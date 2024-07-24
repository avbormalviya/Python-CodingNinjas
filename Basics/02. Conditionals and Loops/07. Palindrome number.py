# Problem statement

""" Check whether a given number ’n’ is a palindrome number.

Note :

Palindrome numbers are the numbers that don't change when reversed.
You don’t need to print anything. Just implement the given function.

Example:

Input: 'n' = 51415
Output: true
Explanation: On reversing, 51415 gives 51415. """

# solution

# taking n as a input

n = int(input())

num = n

reverse = 0

# reversing number n.

while num != 0:
    reverse = reverse * 10 + num % 10
    num //= 10

# checking is palindrome or not.

if reverse == n:
    print("true")
else:
    print("false")
