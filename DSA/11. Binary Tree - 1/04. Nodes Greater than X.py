
# Problem statement

""" For a given a binary tree of integers and an integer X, find and return the total number of nodes of the given
binary tree which are having data greater than X. """


# solution


from binary_tree import BinaryTree


# Function to count the number of nodes with data greater than X in the binary tree
def nodesGreaterThanX(root, x):
    # Base case: if the current node is None, return 0
    if root is None:
        return 0

    # Recursively count in the left subtree
    leftCount = nodesGreaterThanX(root.left, x)

    # Recursively count in the right subtree
    rightCount = nodesGreaterThanX(root.right, x)

    # Return the total count from left, right, and the current node if root.data > x
    return leftCount + rightCount + (1 if root.data > x else 0)


if __name__ == "__main__":
    # Create a BinaryTree instance
    tree = BinaryTree()

    # Input the binary tree using level order
    root = tree.input()

    # Input the value of X
    x = int(input())

    # Print the number of nodes whose data is greater than X
    print(nodesGreaterThanX(root, x))
