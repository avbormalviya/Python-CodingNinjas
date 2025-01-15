
# Problem statement

""" Given two generic trees, return true if they are structurally identical. Otherwise return false.

Structural Identical
If the two given trees are made of nodes with the same values and the nodes are arranged in the same way,
then the trees are called identical. """


# Solution


from generic_tree import GenericTree, Node


def areIdentical(root1, root2):
    """
    Checks if two generic trees are structurally identical.

    Args:
        root1 (Node): The root node of the first tree.
        root2 (Node): The root node of the second tree.

    Returns:
        bool: True if the trees are structurally identical, False otherwise.
    """
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if len(root1.children) != len(root2.children):
        return False

    for child1, child2 in zip(root1.children, root2.children):
        if not areIdentical(child1, child2):
            return False

    return True


if __name__ == "__main__":
    gt1 = GenericTree()
    gt1.input()

    gt2 = GenericTree()
    gt2.input()

    print(areIdentical(gt1.root, gt2.root))
