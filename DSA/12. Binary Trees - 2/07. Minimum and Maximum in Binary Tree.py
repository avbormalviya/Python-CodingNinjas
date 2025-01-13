
# Problem statement

""" For a given a Binary Tree of type integer, find and return the minimum and the maximum data values.

Return the output as an object of Pair class, which is already created.

Note:
All the node data will be unique and hence there will always exist a minimum and maximum node data. """


# Solution


from binary_tree import BinaryTree


class Pair:
    """
    A helper class to store the minimum and maximum values of a binary tree.
    """
    def __init__(self):
        self.min = float('inf')
        self.max = float('-inf')


def minMax(root):
    """
    Computes the minimum and maximum node data values in a binary tree.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        Pair: An object containing the minimum and maximum values in the tree.
    """
    if root is None:
        return Pair()

    # Recursively find min and max in left and right subtrees
    leftPair = minMax(root.left)
    rightPair = minMax(root.right)

    # Compute the overall min and max
    pair = Pair()
    pair.min = min(root.data, leftPair.min, rightPair.min)
    pair.max = max(root.data, leftPair.max, rightPair.max)

    return pair


if __name__ == '__main__':
    # Input the tree
    tree = BinaryTree()
    root = tree.input()

    # Find the minimum and maximum node data
    pair = minMax(root)
    print(pair.min, pair.max)
