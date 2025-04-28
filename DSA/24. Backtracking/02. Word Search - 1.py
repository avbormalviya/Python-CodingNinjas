
# Problem statement

""" You are given a 2D board('N' rows and 'M' columns) of characters and a string 'word'.

Your task is to return true if the given word exists in the grid, else return false.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.

Note:
The same letter cell should not be used more than once.

For Example:
For a given word “design” and the given 2D board
[[q’, ‘v’, ‘m’, ‘h’],
 [‘d’, ‘e’, ‘scratch_KNN.py’, ‘i’],
 [‘d’, ‘g’, ‘f’, ‘g’],
 [‘e’, ‘c’, ‘p’, ‘n’]]

The word design can be formed by sequentially adjacent cells as shown by the highlighted color in the
2nd row and last column. """


# Solution

def isPresent(board, word, row, col):
    def backtrack(i, j, index, visited):
        # Base Case: If all letters are matched
        if index == len(word):
            return True

        # Boundary Conditions & Mismatch Check
        if i < 0 or i >= row or j < 0 or j >= col or (i, j) in visited or board[i][j] != word[index]:
            return False

        # Mark cell as visited
        visited.add((i, j))

        # Explore 4 Directions (Up, Down, Left, Right)
        found = (
            backtrack(i + 1, j, index + 1, visited) or
            backtrack(i - 1, j, index + 1, visited) or
            backtrack(i, j + 1, index + 1, visited) or
            backtrack(i, j - 1, index + 1, visited)
        )

        # Undo visit (Backtracking)
        visited.remove((i, j))

        return found

    # Early exit if word is longer than board cells
    if len(word) > row * col:
        return False

    # Search for the first letter in the board
    for i in range(row):
        for j in range(col):
            if board[i][j] == word[0] and backtrack(i, j, 0, set()):
                return True

    return False


# Input handling
n, m = map(int, input().split())  # Read board dimensions
board = [list(input().strip()) for _ in range(n)]  # Read board
word = input().strip()  # Read word

# Output result
print(isPresent(board, word, n, m))
