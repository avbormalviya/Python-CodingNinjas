
# Problem statement

""" Given a binary tree, return the longest path from leaf to root. Longest means, a path which contain maximum
number of nodes from leaf to root. """


# Solution


from binary_tree import BinaryTree


def longestLeafToRootPath(root):
    if not root:
        return 0, []

    # Recursively find the longest path in the left and right subtrees
    left_depth, left_path = longestLeafToRootPath(root.left)
    right_depth, right_path = longestLeafToRootPath(root.right)

    # Choose the longer path and add the current node'scratch_KNN.py data
    if left_depth > right_depth:
        return left_depth + 1, left_path + [root.data]
    else:
        return right_depth + 1, right_path + [root.data]


if __name__ == "__main__":
    bt = BinaryTree()
    bt.input()  # Assuming BinaryTree.input constructs the binary tree
    depth, path = longestLeafToRootPath(bt.root)
    print(' '.join(map(str, reversed(path))))  # Reverse to print root-to-leaf order
