
# Problem statement

""" Given a generic tree and an integer x, check if x is present in the given tree or not. Return true
if x is present, return false otherwise. """


# Solution


from generic_tree import GenericTree, Node


def containsX(root, x):
    """
    Checks if the tree contains a node with the given value.

    Args:
        root (Node): The root node of the tree.
        x (int): The value to search for.

    Returns:
        bool: True if the value exists in the tree, False otherwise.
    """
    if not root:
        return False

    if root.data == x:
        return True

    for child in root.children:
        if containsX(child, x):
            return True

    return False


if __name__ == "__main__":
    gt = GenericTree()
    gt.input()
    x = int(input())
    print(containsX(gt.root, x))
