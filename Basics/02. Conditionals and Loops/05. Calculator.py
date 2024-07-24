# Problem statement

""" Write a program that performs the tasks of a simple calculator. The program should first take an integer as input
and then based on that integer perform the task as given below.

1. If the input is 1, then 2 integers are taken from the user and their sum is printed.

2. If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.

3. If the input is 3, then 2 integers are taken from the user and their product is printed.

4. If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd
number) is printed.

5. If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.

6. If the input is 6, then the program exits.

7. For any other input, then print "Invalid Operation".
Note: Each answer in next line. """

# solution

# taking input and according to input print output.

while True:
    num = int(input())

    if num == 1:
        first = int(input())
        second = int(input())

        print(int(first + second))

    elif num == 2:
        first = int(input())
        second = int(input())

        print(int(first - second))

    elif num == 3:
        first = int(input())
        second = int(input())

        print(int(first * second))

    elif num == 4:
        first = int(input())
        second = int(input())

        print(int(first / second))

    elif num == 5:
        first = int(input())
        second = int(input())

        print(int(first % second))

    elif num == 6:
        exit()

    else:
        print("Invalid Operation")
