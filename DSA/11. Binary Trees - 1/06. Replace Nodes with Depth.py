
# Problem statement

""" For a given a Binary Tree of integers, replace each of its data with the depth of the tree.

Root is at depth 0, hence the root data is updated with 0. Replicate the same further going down the in the depth
of the given tree.

The modified tree will be printed in the in-order fashion. """


# solution


from binary_tree import BinaryTree


# Function to replace each node'scratch_KNN.py value with its depth and print the depth
def replaceWithDepth(root, depth=0):
    # Base case: If the node is None, return
    if root is None:
        return

    # Set the current node'scratch_KNN.py data to its depth
    root.data = depth

    # Recursively call replaceWithDepth for the left subtree
    replaceWithDepth(root.left, depth + 1)

    # Print the depth of the current node
    print(depth, end=" ")

    # Recursively call replaceWithDepth for the right subtrees
    replaceWithDepth(root.right, depth + 1)


if __name__ == "__main__":
    # Create a BinaryTree instance
    tree = BinaryTree()

    # Input the binary tree using level order
    root = tree.input()

    # Replace nodes with their depths and print the depth of each node
    replaceWithDepth(root)
