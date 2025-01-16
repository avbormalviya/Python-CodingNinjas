
# Problem statement

""" Given the binary Tree and two nodes say ‘p’ and ‘q’. Determine whether the two nodes are cousins of
each other or not. Two nodes are said to be cousins of each other if they are at same level of the Binary
Tree and have different parents.

Do it in O(n). """


# Solution


from binary_tree import BinaryTree


def isCousin(root, p, q):
    if not root:
        return False

    # Helper function to find depth and parent
    def findDepthAndParent(node, target, depth=0, parent=None):
        if not node:
            return None, -1  # Parent is None, depth is -1 (not found)

        if node.data == target:
            return parent, depth

        # Search in left and right subtrees
        left = findDepthAndParent(node.left, target, depth + 1, node)
        if left[0]:  # If found in the left subtree
            return left

        return findDepthAndParent(node.right, target, depth + 1, node)

    # Find depth and parents for both nodes
    parent_p, depth_p = findDepthAndParent(root, p)
    parent_q, depth_q = findDepthAndParent(root, q)

    # Check if they are at the same depth and have different parents
    return depth_p == depth_q and parent_p != parent_q


if __name__ == "__main__":
    bt = BinaryTree()
    bt.input()
    p = int(input())
    q = int(input())
    cousin = isCousin(bt.root, p, q)
    print(cousin)
