# Problem statement

""" Given a 2D integer array with n rows and m columns.Print the 0th row from input n times, 1st row n-1 times…..(n-1)th
row will be printed 1 time. """


# solution

def print2dArray(arr):
    # Iterate through each row by index
    for i in range(len(arr)):
        # Print the current row (len(arr) - i) times
        for _ in range(len(arr) - i):
            print(*arr[i])  # Print the entire row


# Input the number of rows and columns
rows = int(input())
cols = int(input())

# Input the 2D array
arr = [list(map(int, input().split())) for _ in range(rows)]

# Call the function to print the 2D array
print2dArray(arr)
