
# Problem statement

""" Given a BST and an integer k. Find and return the path from the node with data k and root (if a node with data
k is present in given BST) in a list. Return empty list otherwise.

Note: Assume that BST contains all unique elements. """


# Solution


from binary_tree import BinaryTree, Node


def findPathBST(root: Node, k: int) -> list[int]:
    """
    Finds the path from the root of the BST to a node with the value `k`.

    Args:
        root (Node): The root of the BST.
        k (int): The value of the target node.

    Returns:
        list[int]: A list of node values representing the path to `k`.
                   Returns an empty list if the node is not found.
    """
    path = []
    current = root

    while current is not None:
        path.append(current.data)

        if current.data == k:
            return path
        elif current.data > k:
            current = current.left
        else:
            current = current.right

    return []  # Return empty list if node is not found


if __name__ == "__main__":
    # Input the BST
    bt = BinaryTree()
    root = bt.input()

    # Input the target node value
    k = int(input())

    # Find the path to the node
    path = findPathBST(root, k)

    print(' -> '.join(map(str, path)))
