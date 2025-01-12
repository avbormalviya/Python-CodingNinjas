
# Problem statement

""" For a given Binary Tree of integers, find and return the height of the tree. Height is defined as the total number
of nodes along the longest path from the root to any of the leaf node. """


# solution


from binary_tree import BinaryTree


# Function to compute the height of the binary tree
def height(root):
    # Base case: if the root is None, the height is 0 (no nodes)
    if root is None:
        return 0

    # Recursive case: height is 1 + maximum of left and right subtree heights
    return 1 + max(height(root.left), height(root.right))


if __name__ == "__main__":
    # Create an instance of BinaryTree
    tree = BinaryTree()

    # Input the binary tree using level order
    root = tree.input()

    # Calculate and print the height of the tree
    print(height(root))
