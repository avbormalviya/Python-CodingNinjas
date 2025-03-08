
# Problem statement

""" 2048 is a game and you are expected to implement the move function for this game.
Arguments passed to the four functions is the matrix which we are using for 2048
The move function will be returning new matrix after moving the corresponding move.

Implement All The Four Moves Using These Functions -
1. move_up
2. move_down
3. move_left
4. move_right """


import random


# Initialize the game board with zeros and add two starting numbers
def start_game():
    mat = [[0] * 4 for _ in range(4)]  # Create a 4x4 grid filled with zeros
    add_new_number(mat)  # Add the first number
    add_new_number(mat)  # Add the second number
    return mat


# Add a new number (2 or 4) in a random empty cell
def add_new_number(grid):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if grid[r][c] == 0]  # Find all empty cells
    if empty_cells:
        r, c = random.choice(empty_cells)  # Choose a random empty cell
        grid[r][c] = 2 if random.random() < 0.9 else 4  # 90% chance of getting a 2, 10% chance of getting a 4


# Shift all numbers to the left, filling empty spaces
def compress(grid):
    new_grid = [[0] * 4 for _ in range(4)]  # Create a new empty grid
    for i in range(4):
        pos = 0  # Position to place the next number
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]  # Move the number to the leftmost available position
                pos += 1
    return new_grid


# Merge adjacent equal numbers in a row
def merge(grid):
    for i in range(4):
        for j in range(3):  # Check up to the second last column
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] *= 2  # Merge the two numbers
                grid[i][j + 1] = 0  # Remove the merged number from its original position
    return grid


# Reverse the rows of the grid (used for right moves)
def reverse(grid):
    return [row[::-1] for row in grid]


# Transpose the grid (convert rows to columns and vice versa, used for up/down moves)
def transpose(grid):
    return [list(row) for row in zip(*grid)]


# Move tiles to the left
def move_left(grid):
    compressed_grid = compress(grid)  # Shift numbers left
    merged_grid = merge(compressed_grid)  # Merge adjacent equal numbers
    final_grid = compress(merged_grid)  # Shift numbers left again to fill gaps
    add_new_number(final_grid)  # Add a new number to the grid
    return final_grid


# Move tiles to the right
def move_right(grid):
    reversed_grid = reverse(grid)  # Reverse the grid to simulate left move
    moved_grid = move_left(reversed_grid)  # Move left
    return reverse(moved_grid)  # Reverse back to original orientation


# Move tiles up
def move_up(grid):
    transposed_grid = transpose(grid)  # Transpose to treat columns as rows
    moved_grid = move_left(transposed_grid)  # Move left (which is actually up)
    return transpose(moved_grid)  # Transpose back to original orientation


# Move tiles down
def move_down(grid):
    transposed_grid = transpose(grid)  # Transpose to treat columns as rows
    moved_grid = move_right(transposed_grid)  # Move right (which is actually down)
    return transpose(moved_grid)  # Transpose back to original orientation


# Print the current grid state
def print_grid(grid):
    for row in grid:
        print(row)


# Main function to run the game loop
def main():
    mat = start_game()
    print_grid(mat)  # Display the initial board state
    while True:
        move = input("Enter move (1: Up, 2: Down, 3: Left, 4: Right): ")  # Get user input
        if move == '1':
            mat = move_up(mat)
        elif move == '2':
            mat = move_down(mat)
        elif move == '3':
            mat = move_left(mat)
        elif move == '4':
            mat = move_right(mat)
        else:
            print("Invalid move. Try again.")
            continue
        print_grid(mat)  # Print the updated board
        if not any(0 in row for row in mat):  # Check if there are no empty cells
            print("Game Over!")
            break


if __name__ == "__main__":
    main()
