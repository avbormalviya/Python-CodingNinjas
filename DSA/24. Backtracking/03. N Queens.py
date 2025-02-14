
# Problem statement

""" You are given an integer 'N'. For a given 'N' x 'N' chessboard, find a way to place 'N'
queens such that no queen can attack any other queen on the chessboard.

A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens.
You have to print all such configurations. """


# Solution


def solveNQueens(n):
    def isSafe(board, row, col):
        # Check same column for previous rows
        for i in range(row):
            if board[i] == col:
                return False

            # Check left diagonal
            if abs(board[i] - col) == abs(i - row):
                return False

        return True

    def solve(board, row):
        if row == n:
            result.append([" . " * c + " Q " + " . " * (n - c - 1) for c in board])
            return

        for col in range(n):
            if isSafe(board, row, col):
                board[row] = col  # Place queen
                solve(board, row + 1)  # Recur for next row
                board[row] = -1  # Backtrack

    result = []
    board = [-1] * n  # Store column positions for each row
    solve(board, 0)

    if not result:
        print("Not possible")
    else:
        for solution in result:
            for row in solution:
                print(row)
            print()


# Input
n = int(input())
solveNQueens(n)
