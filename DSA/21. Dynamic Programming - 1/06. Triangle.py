
# Problem statement

""" You are given a triangular array/list 'TRIANGLE'. Your task is to return the minimum path sum to reach from
the top to the bottom row.

The triangle array will have N rows and the i-th row, where 0 <= i < N will have i + 1 elements.

You can move only to the adjacent number of row below each step. For example, if you are at index j in row i,
then you can move to i or i + 1 index in row j + 1 in each step.

For Example :
If the array given is 'TRIANGLE' = [[1], [2,3], [3,6,7], [8,9,6,1]] the triangle array will look like:

1
2,3
3,6,7
8,9,6,10

For the given triangle array the minimum sum path would be 1->2->3->8. Hence the answer would be 14. """


# Solution


def minimumPathSum(triangle, n, dp):
    # Start from the second last row and move upwards
    for row in range(n - 2, -1, -1):  # Start from second last row, row = n-2
        for col in range(len(triangle[row])):  # Process each element in the row
            # Update dp[col] to store the minimum path sum at the current position
            dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

    return dp[0]  # The result is now stored at dp[0]


# Input the number of rows in the triangle
n = int(input())

# Input the triangle
triangle = [list(map(int, input().split())) for _ in range(n)]

# Initialize the dp array as the last row of the triangle
dp = triangle[n - 1][:]  # Copy the last row to dp

# Call the function and print the result
print(minimumPathSum(triangle, n, dp))
