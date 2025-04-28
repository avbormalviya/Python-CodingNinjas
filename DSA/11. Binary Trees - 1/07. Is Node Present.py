
# Problem statement

# For a given Binary Tree of type integer and a number X, find whether a node exists in the tree with data X or not.


# solution


from binary_tree import BinaryTree


# Function to check if a node with value x is present in the tree
def isNodePresent(root, x):
    # Base case: if the current node is None, return False
    if root is None:
        return False

    # If the current node'scratch_KNN.py data is equal to x, return True
    if root.data == x:
        return True

    # Recursively check the left and right subtrees
    return isNodePresent(root.left, x) or isNodePresent(root.right, x)


if __name__ == "__main__":
    # Create an instance of BinaryTree
    tree = BinaryTree()

    # Input the binary tree using level order
    tree.input()

    # Input the value to check
    x = int(input())

    # Check if the node with value x is present in the tree
    print(isNodePresent(tree.root, x))
