
# Problem statement

""" Given a chain of matrices A1, A2, A3,.....An. Your task is to find out the minimum cost to multiply these matrices. The cost of matrix multiplication is defined as the number of scalar multiplications. A Chain of matrices A1, A2, A3,.....An is represented by a sequence of numbers in an array ‘arr’ where the dimension of 1st matrix is equal to arr[0] * arr[1] , 2nd matrix is arr[1] * arr[2], and so on.

For example:
For arr[ ] = { 10, 20, 30, 40}, matrix A1 = [10 * 20], A2 = [20 * 30], A3 = [30 * 40]

Scalar multiplication of matrix with dimension 10 * 20 is equal to 200. """


# Solution


def matrixMultiplication(matrix, i, j, dp):
    """
    Function to find the minimum number of scalar multiplications needed
    to multiply a sequence of matrices using memoization.

    Parameters:
    - matrix: List of matrix dimensions.
    - i: Starting index of the matrix chain.
    - j: Ending index of the matrix chain.
    - dp: Memoization table to store already computed results.

    Returns:
    - The minimum multiplication cost.
    """

    # Base case: If there is only one matrix, no multiplication is needed
    if i == j:
        return 0

        # If the subproblem is already computed, return the stored result
    if dp[i][j] != -1:
        return dp[i][j]

        # Initialize minCost with a large value
    minCost = float('inf')

    # Try every possible way to split the matrix chain at index k
    for k in range(i, j):
        # Recursively calculate the cost of multiplying two partitions
        leftMinCost = matrixMultiplication(matrix, i, k, dp)
        rightMinCost = matrixMultiplication(matrix, k + 1, j, dp)

        # Compute the cost of multiplying the two resulting matrices
        cost = leftMinCost + rightMinCost + (matrix[i] * matrix[k + 1] * matrix[j + 1])

        # Update minCost if the current split results in a lower cost
        minCost = min(minCost, cost)

    # Store the result in the DP table before returning
    dp[i][j] = minCost
    return dp[i][j]


# Input Handling
n = int(input())  # Number of matrices
matrix = list(map(int, input().split()))  # Read matrix dimensions

# Initialize the DP table with -1 (indicating uncomputed subproblems)
dp = [[-1] * n for _ in range(n)]

# Solve for the full matrix chain (from 0 to n-2)
print(matrixMultiplication(matrix, 0, n - 2, dp))
