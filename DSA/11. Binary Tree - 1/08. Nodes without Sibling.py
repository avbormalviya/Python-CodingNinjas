
# Problem statement

""" For a given Binary Tree of type integer, print all the nodes without any siblings.

Example Input :
1 4 5 6 -1 -1 7 20 30 80 90 -1 -1 -1 -1 -1 -1 -1 -1

Explanation:
In respect to the root, node data in the left subtree that satisfy the condition of not having a sibling would be 6, taken in a top-down sequence. Similarly, for the right subtree, 7 is the node data without any sibling.

Since we print the siblings in the left-subtree first and then the siblings from the right subtree, taken in a top-down fashion, we print 6 7.

Example Output:
6 7   """


# solution


from binary_tree import BinaryTree


# Function to print nodes that do not have siblings
def printNodesWithoutSibling(root):
    # Base case: If the node is None, do nothing
    if root is None:
        return

    # Check if the node has a left child but no right child
    if root.left is not None and root.right is None:
        # Print the data of the left child as it has no sibling
        print(root.left.data, end=" ")

    # Check if the node has a right child but no left child
    if root.left is None and root.right is not None:
        # Print the data of the right child as it has no sibling
        print(root.right.data, end=" ")

    # Recursively check the left subtree for nodes without siblings
    printNodesWithoutSibling(root.left)

    # Recursively check the right subtree for nodes without siblings
    printNodesWithoutSibling(root.right)

    return  # End the function


# Main block of code to execute when the script is run directly
if __name__ == "__main__":
    # Create an instance of the BinaryTree class
    tree = BinaryTree()

    # Input the binary tree using level-order traversal (method defined in BinaryTree class)
    tree.input()

    # Call the printNodesWithoutSibling function on the root of the tree
    # This will print all nodes in the tree that do not have siblings
    printNodesWithoutSibling(tree.root)
