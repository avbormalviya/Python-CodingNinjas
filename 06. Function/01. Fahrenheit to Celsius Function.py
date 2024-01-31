# Problem statement

""" Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all
 Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

Note: You don't have to write the main function or take input. It has already been taken care of and you need to just
print the integer value . Just write the code that prints Fahrenheit to Celsius table in the function itself. """


# solution

def printTable(start, end, step):
    for i in range(start, end + 1, step):
        print(i, end='\t')
        print(int(((i - 32) * 5) / 9))


s = int(input())
e = int(input())
step = int(input())
printTable(s, e, step)
