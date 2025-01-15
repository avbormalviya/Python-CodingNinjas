
# Problem statement

# Given a generic tree, find and return the sum of all nodes present in the given tree.


# Solution

from generic_tree import GenericTree


def sumOfNodes(root):
    """
    Recursively calculates the sum of all nodes in the generic tree.

    Args:
        root (Node): The root node of the tree or subtree.

    Returns:
        int: The sum of all nodes in the tree.
    """
    if root is None:
        return 0

    # Sum the data of the current node and its children
    childrenSum = sum(sumOfNodes(child) for child in root.children)
    return root.data + childrenSum


if __name__ == "__main__":
    gt = GenericTree()
    gt.input()
    print(sumOfNodes(gt.root))
    