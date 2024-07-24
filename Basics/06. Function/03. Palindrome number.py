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

def isPalindrome(n):
    rev = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10

    return rev


n = int(input())

if n != isPalindrome(n):
    print('false')
else:
    print('true')
