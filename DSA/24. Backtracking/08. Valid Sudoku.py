
# Problem statement

""" You have been given a 9 X 9 2D matrix 'MATRIX' with some cells filled with digits(1 - 9),
and some empty cells (denoted by 0).

You need to find whether there exists a way to fill all the empty cells with some digit(1 - 9)
such that the final matrix is a valid Sudoku solution.

A Sudoku solution must satisfy all the following conditions-
1. Each of the digits 1 - 9 must occur exactly once in each row.
2. Each of the digits 1 - 9 must occur exactly once in each column.
3. Each of the digits 1 - 9 must occur exactly once in each of the 9, 3 x 3 sub-matrices of the matrix.

Note
1. There will always be a cell in the matrix which is empty.
2. The given initial matrix will always be consistent according to the rules mentioned in the problem statement. """


# Solution


def is_valid(board, row, col, num):
    """
    Check if it'scratch_KNN.py valid to place `num` at board[row][col].
    Ensures no duplicate in the row, column, and 3x3 subgrid.
    """
    # Check the row and column for duplicates
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Determine the top-left corner of the 3x3 subgrid
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)

    # Check the 3x3 subgrid for duplicates
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True  # If no conflicts, placement is valid


def solve_sudoku(board):
    """
    Solve Sudoku using backtracking.
    Finds an empty cell and tries placing numbers 1-9 recursively.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):  # Check if placement is valid
                        board[row][col] = num  # Place the number

                        if solve_sudoku(board):  # Recursively try to solve the rest
                            return True

                        board[row][col] = 0  # Backtrack if solution isn't found

                return False  # No valid number found, trigger backtracking

    return True  # Solution found, all cells filled correctly


# Input Sudoku board
board = [list(map(int, input().split())) for _ in range(9)]

# Solve and print the result
if solve_sudoku(board):
    for row in board:
        print(*row)
else:
    print("No solution exists.")
