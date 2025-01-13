
# Problem statement

""" For a given Binary Tree of type integer and a number K, print out all root-to-leaf paths where the sum of all
the node data along the path is equal to K.

If you see in the above-depicted picture of Binary Tree, we see that there are a total of two paths, starting from
the root and ending at the leaves which sum up to a value of K = 13.

The paths are:
a. 2 3 4 4
b. 2 3 8

One thing to note here is, there is another path in the right sub-tree in reference to the root, which sums up
to 13 but since it doesn't end at the leaf, we discard it.

The path is: 2 9 2(not a leaf) """


# Solution


from binary_tree import BinaryTree, Node


def printPathsHelper(root, k, path, pathSum):
    """
    Helper function for recursively finding and printing all paths
    with a sum equal to k in the binary tree.

    Args:
        root (Node): The current node in the binary tree.
        k (int): The target sum for the paths.
        path (list): A list to store the current path.
        pathSum (int): The cumulative sum of the current path.
    """
    if root is None:
        return

    # Add current node to path and update the cumulative sum
    path.append(root.data)
    pathSum += root.data

    # If it's a leaf node and the path sum matches k, print the path
    if root.left is None and root.right is None and pathSum == k:
        print(" -> ".join(map(str, path)))

    # Recur for left and right subtrees
    printPathsHelper(root.left, k, path, pathSum)
    printPathsHelper(root.right, k, path, pathSum)

    # Backtrack: Remove the current node from the path
    path.pop()


def printPaths(root, k):
    """
    Finds and prints all paths in the binary tree where the sum of node values equals k.

    Args:
        root (Node): The root of the binary tree.
        k (int): The target sum for the paths.
    """
    if root is None:
        print("The tree is empty.")
        return

    printPathsHelper(root, k, [], 0)


if __name__ == '__main__':
    # Input the tree
    tree = BinaryTree()
    root = tree.input()

    # Input the value of K
    k = int(input())

    # Print the paths with sum K
    printPaths(root, k)
