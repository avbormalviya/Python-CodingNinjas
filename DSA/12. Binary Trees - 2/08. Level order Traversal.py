
# Problem statement

""" For a given a Binary Tree of type integer, print it in a level order fashion where each level will be printed on
a new line. Elements on every level will be printed in a linear fashion and a single space will separate them. """


# Solution

from binary_tree import BinaryTree
from collections import deque


def printLevelWise(root):
    """
    Prints the binary tree level by level in a breadth-first manner.

    Args:
        root (Node): The root node of the binary tree.
    """
    if root is None:
        print("The tree is empty.")
        return

    q = deque()
    q.append(root)

    level = 0
    while len(q) > 0:
        count = len(q)
        print(f"Level {level}: ", end='')

        while count > 0:
            curr = q.popleft()
            print(curr.data, end=' ')

            if curr.left is not None:
                q.append(curr.left)

            if curr.right is not None:
                q.append(curr.right)

            count -= 1

        print()  # Move to the next line for the next level
        level += 1


if __name__ == '__main__':
    # Input the tree
    tree = BinaryTree()
    root = tree.input()

    # Print the tree in level order
    printLevelWise(root)
