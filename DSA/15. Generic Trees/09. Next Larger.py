
# Problem statement

""" Given a generic tree and an integer n. Find and return the node with next larger element in the tree i.e.
find a node with value just greater than n.

Note:
Return NULL if no node is present with the value greater than n. """


# Solution


from generic_tree import GenericTree, Node


def nextLargerElement(root, n):
    """
    Finds the first node in the tree whose data is greater than n.

    Args:
        root (Node): The root node of the tree.
        n (int): The value to compare with.

    Returns:
        Optional[Node]: The first node whose data is greater than n, or None if no such node exists.
    """
    if not root:
        return None

    # Check the root node first
    if root.data > n:
        return root

    # Recursively check the children
    for child in root.children:
        next_larger = nextLargerElement(child, n)
        if next_larger:
            return next_larger

    return None


if __name__ == "__main__":
    gt = GenericTree()
    gt.input()
    n = int(input())
    print(nextLargerElement(gt.root, n).data)
