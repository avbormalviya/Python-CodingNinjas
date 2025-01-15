
# Problem statement

""" Given a generic tree, find and return the node with maximum data.

Note: Return null if the tree is empty. """


# Solution


from generic_tree import GenericTree


def maxDataNodeIterative(root):
    """
    Finds the maximum data value in the generic tree using an iterative approach.

    Args:
        root (Node): The root node of the tree or subtree.

    Returns:
        Optional[int]: The maximum data value, or None if the tree is empty.
    """
    if root is None:
        return None

    max_data = float('-inf')  # Initialize max_data with the smallest possible value
    stack = [root]  # Use a stack to simulate tree traversal

    while stack:
        current = stack.pop()  # Get the current node
        max_data = max(max_data, current.data)  # Update max_data if needed

        # Add all children of the current node to the stack
        stack.extend(current.children)

    return max_data


if __name__ == "__main__":
    gt = GenericTree()
    gt.input()
    print(maxDataNodeIterative(gt.root))
    