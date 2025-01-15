
# Problem statement

""" Given a Binary Search Tree and two integers k1 and k2, find and print the elements which are in range
k1 and k2 (both inclusive).

Print the elements in increasing order. """


# Solution


from binary_tree import BinaryTree, Node


def elementsInRangeK1K2(root: Node, k1: int, k2: int) -> None:
    """
    Prints all elements in the range [k1, k2] from the BST in ascending order.

    Args:
        root (Node): The root of the BST.
        k1 (int): The lower bound of the range.
        k2 (int): The upper bound of the range.
    """
    if root is None:
        return

    # Traverse left subtree if the current node might have values >= k1
    if root.data > k1:
        elementsInRangeK1K2(root.left, k1, k2)

    # Print the current node if it's within the range
    if k1 <= root.data <= k2:
        print(root.data, end=' ')

    # Traverse right subtree if the current node might have values <= k2
    if root.data < k2:
        elementsInRangeK1K2(root.right, k1, k2)


if __name__ == '__main__':
    # Input the BST
    tree = BinaryTree()
    root = tree.input()

    # Input the range
    k1, k2 = map(int, input().split())

    # Print the elements in the range [k1, k2]
    elementsInRangeK1K2(root, k1, k2)
