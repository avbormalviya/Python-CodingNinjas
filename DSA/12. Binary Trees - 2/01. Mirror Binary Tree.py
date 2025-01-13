
# Problem statement

# For a given Binary Tree of type integer, update it with its corresponding mirror image.


# solution


from binary_tree import BinaryTree


def mirrorBinaryTree(root):
    """
    Recursively mirrors a binary tree by swapping the left and right children
    of all nodes in the tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        The root of the mirrored binary tree.
    """
    if root is None:
        # Base case: If the current node is None, there's nothing to mirror
        return None

    # Recursively mirror the left subtree
    left = mirrorBinaryTree(root.left)
    # Recursively mirror the right subtree
    right = mirrorBinaryTree(root.right)

    # Swap the left and right children of the current node
    root.left = right
    root.right = left

    return root


if __name__ == '__main__':
    # Initialize a binary tree using the BinaryTree class
    tree = BinaryTree()

    # Build the binary tree based on user input
    tree.input()

    # Print the original tree structure
    tree.print()

    # Mirror the binary tree starting from the root
    mirrorBinaryTree(tree.root)

    # Print the mirrored tree structure
    tree.print()
