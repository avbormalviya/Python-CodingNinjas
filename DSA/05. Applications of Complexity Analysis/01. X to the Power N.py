
# Problem statement

""" Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to return the answer.

Do this recursively. """


# solution


def findPowerOfANumber(x, n):
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return x

    # Divide and conquer approach
    half_power = findPowerOfANumber(x, n // 2)

    # If n is even, square the result
    if n % 2 == 0:
        return half_power * half_power
    # If n is odd, multiply by x
    else:
        return x * half_power * half_power


# Input the base and exponent
x = int(input())
n = int(input())

# Output the result
print(findPowerOfANumber(x, n))
