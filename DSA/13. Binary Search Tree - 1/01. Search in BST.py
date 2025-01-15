# Problem statement

""" Given a BST and an integer k. Find if the integer k is present in given BST or not. You have to return true,
if node with data k is present, return false otherwise.

Note:
Assume that BST contains all unique elements. """

# Solution


from binary_tree import BinaryTree, Node


def searchInBST(root: Node, k: int) -> bool:
    """
    Searches for a key in a Binary Search Tree (BST).

    Args:
        root (Node): The root of the BST.
        k (int): The key to search for.

    Returns:
        bool: True if the key is found, False otherwise.
    """
    if root is None:
        return False

    if root.data == k:
        return True

    if root.data > k:
        return searchInBST(root.left, k)
    else:
        return searchInBST(root.right, k)


if __name__ == '__main__':
    # Input the BST
    tree = BinaryTree()
    root = tree.input()

    # Input the key to search
    k = int(input())

    # print Result
    print(searchInBST(root, k))
