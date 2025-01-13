
# Problem statement

""" You are given the root node of a binary tree.Print its preorder traversal. """


# solution


from binary_tree import BinaryTree


# Preorder Traversal: Root -> Left -> Right
def preorder(root):
    # Base case: If the node is None, return
    if root is None:
        return

    # Print the data of the current node
    print(root.data, end=" ")

    # Recursively visit the left subtree
    preorder(root.left)

    # Recursively visit the right subtree
    preorder(root.right)


if __name__ == "__main__":
    tree = BinaryTree()

    # Input the binary tree using level order
    root = tree.input()

    # Perform and print the preorder traversal of the tree
    preorder(root)
