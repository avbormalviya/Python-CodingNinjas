
# Problem statement

""" For a given Binary Tree of integers, find and return the sum of all the nodes data. """


# solution


from binary_tree import BinaryTree


# Function to calculate the sum of all nodes in a binary tree
def sumOfNodes(root):
    # Base case: if the node is None, return 0
    if root is None:
        return 0

    # Recursive case: sum up the current node's data, left subtree, and right subtree
    return root.data + sumOfNodes(root.left) + sumOfNodes(root.right)


if __name__ == "__main__":
    # Create an instance of BinaryTree
    tree = BinaryTree()

    # Input the tree structure (this function is assumed to be defined in the BinaryTree class)
    root = tree.input()

    # Print the sum of all nodes in the tree
    print(sumOfNodes(root))
