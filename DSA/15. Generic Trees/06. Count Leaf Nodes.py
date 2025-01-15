
# Problem statement

# Given a generic tree, count and return the number of leaf nodes present in the given tree.


# Solution


from generic_tree import GenericTree, Node


def countLeafNodes(root):
    """
    Counts the number of leaf nodes in a generic tree.

    Args:
        root (Node): The root node of the tree.

    Returns:
        int: The number of leaf nodes.
    """
    if root is None:
        return 0

    # A node is a leaf if it has no children
    if len(root.children) == 0:
        return 1

    # Recursively count leaf nodes in all subtrees
    return sum(countLeafNodes(child) for child in root.children)


if __name__ == "__main__":
    gt = GenericTree()
    gt.input()
    print(countLeafNodes(gt.root))
