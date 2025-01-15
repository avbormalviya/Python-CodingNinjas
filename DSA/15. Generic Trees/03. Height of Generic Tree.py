
# Problem statement

""" Given a generic tree, find and return the height of given tree. The height of a tree is defined as the
longest distance from root node to any of the leaf node. Assume the height of a tree with a single node is 1. """


# Solution

from generic_tree import GenericTree
from typing import Optional


def heightOfGenericTree(root: Optional['Node']) -> int:
    """
    Calculates the height of a generic tree.

    Args:
        root (Node): The root node of the tree.

    Returns:
        int: The height of the tree.
    """
    if root is None:
        return 0

    # Recursively find the height of all child subtrees
    child_heights = [heightOfGenericTree(child) for child in root.children]

    # The height of the tree is 1 + the maximum child height
    return 1 + max(child_heights, default=0)  # Use default=0 for leaf nodes


if __name__ == "__main__":
    gt = GenericTree()
    gt.input()
    print(heightOfGenericTree(gt.root))
