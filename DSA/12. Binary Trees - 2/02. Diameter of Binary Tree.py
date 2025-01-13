

# Problem statement

""" For a given Binary of type integer, find and return the ‘Diameter’.

Diameter of a Tree
The diameter of a tree can be defined as the maximum distance between two leaf nodes.
Here, the distance is measured in terms of the total number of nodes present along the path of the two leaf nodes,
including both the leaves. """


# solution


from binary_tree import BinaryTree


def diameterOfBinaryTree(root):
    """
    Calculates the diameter of a binary tree.

    The diameter of a binary tree is the length of the longest path between
    any two nodes in the tree. This path may or may not pass through the root.

    Args:
        root: The root node of the binary tree.

    Returns:
        A tuple (height, diameter):
        - height: The height of the current subtree.
        - diameter: The diameter of the current subtree.
    """
    if root is None:
        # Base case: If the current node is None, the height and diameter are 0
        return 0, 0

    # Recursively calculate the height and diameter of the left subtree
    leftHeight, leftDiameter = diameterOfBinaryTree(root.left)

    # Recursively calculate the height and diameter of the right subtree
    rightHeight, rightDiameter = diameterOfBinaryTree(root.right)

    # Calculate the height of the current node
    height = 1 + max(leftHeight, rightHeight)

    # Calculate the diameter of the current subtree
    # The diameter is the largest value among:
    # 1. The path passing through the current node (leftHeight + rightHeight + 1)
    # 2. The diameter of the left subtree
    # 3. The diameter of the right subtree
    diameter = max(leftHeight + rightHeight + 1, leftDiameter, rightDiameter)

    return height, diameter


if __name__ == '__main__':
    # Initialize a binary tree using the BinaryTree class
    tree = BinaryTree()

    # Build the binary tree based on user input
    tree.input()

    # Find the diameter of the binary tree starting from the root
    height, diameter = diameterOfBinaryTree(tree.root)

    # Print the diameter of the binary tree
    print(diameter)
