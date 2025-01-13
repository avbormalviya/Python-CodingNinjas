
# Problem statement

""" You are given a Binary Tree of type integer, a integer value of target node's data, and an integer value K.

Print the data of all nodes that have a distance K from the target node. The order in which they would be
printed will not matter. """


# Solution


from binary_tree import BinaryTree, Node


def printNodesAtDepthK(root, k):
    """
    Prints all nodes at a depth K from the given root.

    Args:
        root (Node): The root node to start the depth search.
        k (int): The depth at which nodes should be printed.
    """
    if root is None:
        return

    if k == 0:
        print(root.data, end=' ')
        return

    printNodesAtDepthK(root.left, k - 1)
    printNodesAtDepthK(root.right, k - 1)


def printNodesAtDistanceK(root, target, k):
    """
    Prints all nodes at a distance K from the target node.

    Args:
        root (Node): The root of the binary tree.
        target (int): The value of the target node.
        k (int): The distance from the target node.

    Returns:
        int: Distance of the target node from the current root.
    """
    if root is None:
        return -1

    # If the current node is the target node
    if root.data == target:
        printNodesAtDepthK(root, k)
        return 0

    # Check in the left subtree
    leftDistance = printNodesAtDistanceK(root.left, target, k)
    if leftDistance != -1:
        if leftDistance + 1 == k:
            print(root.data, end=' ')
        else:
            printNodesAtDepthK(root.right, k - leftDistance - 2)
        return leftDistance + 1

    # Check in the right subtree
    rightDistance = printNodesAtDistanceK(root.right, target, k)
    if rightDistance != -1:
        if rightDistance + 1 == k:
            print(root.data, end=' ')
        else:
            printNodesAtDepthK(root.left, k - rightDistance - 2)
        return rightDistance + 1

    return -1


if __name__ == '__main__':
    # Input the tree
    tree = BinaryTree()
    root = tree.input()

    # Input the target node and K

    target = int(input())
    k = int(input())

    # Print nodes at distance K from the target node
    printNodesAtDistanceK(root, target, k)
