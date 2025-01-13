
# Problem statement

# For a given Binary Tree of integers, print the post-order traversal.


# solution


from binary_tree import BinaryTree


# Postorder Traversal: Left -> Right -> Root
def postorder(root):
    # Base case: If the node is None, return
    if root is None:
        return

    # Recursively visit the left subtree
    postorder(root.left)

    # Recursively visit the right subtree
    postorder(root.right)

    # Print the data of the current node (after left and right subtrees)
    print(root.data, end=" ")


if __name__ == "__main__":
    # Create a BinaryTree instance
    tree = BinaryTree()

    # Input the binary tree using level order
    root = tree.input()

    # Perform and print the postorder traversal of the tree
    postorder(root)
