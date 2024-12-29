
# Problem statement

""" Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move
all disks from source rod to destination rod using third rod (say auxiliary). The rules are :

1) Only one disk can be moved at a time.
2) A disk can be moved only if it is on the top of a rod.
3) No disk can be placed on the top of a smaller disk.
Print the steps required to move n disks from source rod to destination rod.

Source Rod is named as 'a', auxiliary rod as 'b' and destination rod as 'c'. """


# solution


def towerOfHanoi(n, s, h, t, moves=None):
    """
    Solves the Tower of Hanoi problem for 'n' disks and returns the sequence of moves.

    Parameters:
    n (int): Number of disks to move.
    s (str): Source rod.
    h (str): Helper rod.
    t (str): Target rod.
    moves (list): List to store the sequence of moves.

    Returns:
    list: Sequence of moves required to solve the Tower of Hanoi problem.
    """

    # Initialize the moves list if it's the first call
    if moves is None:
        moves = []

    # Base case: If there is only one disk, move it directly from source to target
    if n <= 1:
        moves.append(f"{s} --> {t}")
        return moves

    # Step 1: Move the top (n-1) disks from source to helper using target as auxiliary
    towerOfHanoi(n - 1, s, t, h, moves)

    # Step 2: Move the nth disk (largest) from source to target
    moves.append(f"{s} --> {t}")

    # Step 3: Move the (n-1) disks from helper to target using source as auxiliary
    towerOfHanoi(n - 1, h, s, t, moves)

    # Return the list of moves
    return moves


# Input: Number of disks
n = int(input())

# Solve the Tower of Hanoi problem and get the moves
moves = towerOfHanoi(n, 'a', 'b', 'c')

# Print each move in a new line
print("\n".join(moves))
