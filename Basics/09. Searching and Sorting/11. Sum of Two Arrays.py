# Problem statement

""" Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively. Both the arrays/lists
 contain numbers from 0 to 9(i.e. single digit integer is present at every index). The idea here is to represent each
 array/list as an integer in itself of digits N and M.

You need to find the sum of both the input arrays/list treating them as two integers and put the result in another
array/list i.e. output array/list will also contain only single digit at every index.

Note:
The sizes N and M can be different.

Output array/list(of all 0s) has been provided as a function argument. Its size will always be one more than the size
of the bigger array/list. Place 0 at the 0th index if there is no carry.

No need to print the elements of the output array/list.
Using the function "sumOfTwoArrays", write the solution to the problem and store the answer inside this output
array/list. The main code will handle the printing of the output on its own. """


# solution


def sumOfTwoArrays(n, arr1, m, arr2):
    # Ensure both arrays have the same length by padding the shorter one with zeros at the beginning
    if n < m:
        arr1 = [0] * (m - n) + arr1
    elif n > m:
        arr2 = [0] * (n - m) + arr2

    carry = 0  # To handle carry-over during addition
    result = []  # To store the final sum of the two arrays

    # Perform addition from the least significant digit to the most significant digit
    for a, b in zip(reversed(arr1), reversed(arr2)):
        # Add corresponding digits and the carry
        total = a + b + carry
        result.append(total % 10)  # Store the last digit of the sum
        carry = total // 10  # Update the carry (integer division by 10)

    # If there'scratch_KNN.py any carry left after the final addition, add it to the result
    if carry:
        result.append(carry)

    # Reverse the result to get the correct order and return it
    return result[::-1]


# Input Handling
n = int(input())
arr1 = [int(input()) for i in range(n)]

m = int(input())
arr2 = [int(input()) for i in range(m)]

# Output the result
print(sumOfTwoArrays(n, arr1, m, arr2))
