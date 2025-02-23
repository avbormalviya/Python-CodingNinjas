
# Problem statement

""" Given a NxM matrix containing Uppercase English Alphabets only. Your task is to tell
if there is a path in the given matrix which makes the sentence “CODINGNINJA” .

There is a path from any cell to all its neighbouring cells. For a particular cell, neighbouring cells are
those cells that share an edge or a corner with the cell. """


# Solution

moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
word = "CODINGNINJA"


def DFS(matrix, n, m, row, col, index, visited):
    """
    Perform DFS to check if the word 'CODINGNINJA' can be found in the grid.

    Parameters:
    - matrix: 2D character grid
    - n, m: Dimensions of the grid
    - row, col: Current cell coordinates
    - index: Current index in the word
    - visited: 2D list to track visited cells

    Returns:
    - 1 if the word is found, else 0
    """
    if index == len(word):  # If we've found all characters
        return 1

    # Boundary conditions + character check + already visited check
    if row < 0 or row >= n or col < 0 or col >= m or matrix[row][col] != word[index] or visited[row][col]:
        return 0

    visited[row][col] = True  # Mark as visited

    # Try all 8 possible moves
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if DFS(matrix, n, m, new_row, new_col, index + 1, visited):
            return 1

    visited[row][col] = False  # Backtrack
    return 0


def isPath(matrix, n, m):
    """
    Check if 'CODINGNINJA' exists in the grid by trying to start DFS from each cell.

    Returns:
    - 1 if the word is found, else 0
    """
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == word[0]:  # If the first letter matches
                visited = [[False] * m for _ in range(n)]  # Reset visited matrix
                if DFS(matrix, n, m, i, j, 0, visited):
                    return 1  # Return immediately if found

    return 0  # Not found


# Input handling
n, m = map(int, input().split())  # Grid dimensions
matrix = [list(input().strip()) for _ in range(n)]  # Read grid input
print(isPath(matrix, n, m))  # Output result
