# Problem statement

""" Given an integer n, find if n is positive, negative or 0.

If n is positive, print "Positive"
If n is negative, print "Negative"
And if n is equal to 0, print "Zero". """

# solution

# taking integer as input

number = int(input())

# checking integer is Positive, Negative or Zero and print

if number < 0:
    print("Negative")

elif number > 0:
    print("Positive")

else:
    print("Zero")
