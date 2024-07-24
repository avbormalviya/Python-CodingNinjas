# Problem statement

""" Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W),you need to convert
all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

# Hint : Use type casting """

# solution

# taking input Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W)

S = int(input())
E = int(input())
W = int(input())

# calculate corresponding Celsius values and print the table.

while S <= E:
    print(S, int((S - 32) * 5 / 9))
    S += W
