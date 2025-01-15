
# Problem statement

""" Given a sorted integer array A of size n, which contains all unique elements. You need to construct a balanced
BST from this input array. Return the root of constructed BST.

Note: If array size is even, take first mid as root. """


# Solution


from binary_tree import BinaryTree, Node


def constructBST(arr: list[int], start: int, end: int) -> Node:
    """
    Constructs a balanced Binary Search Tree (BST) from a sorted array.

    Args:
        arr (list[int]): The sorted array of integers.
        start (int): The starting index of the current subarray.
        end (int): The ending index of the current subarray.

    Returns:
        Node: The root of the constructed BST.
    """
    if start > end:
        return None

    # Find the middle element to use as root
    mid = (start + end) // 2
    root = Node(arr[mid])

    # Recursively construct the left and right subtrees
    root.left = constructBST(arr, start, mid - 1)
    root.right = constructBST(arr, mid + 1, end)

    return root


if __name__ == "__main__":
    # Input: Sorted array
    arr = list(map(int, input().split()))

    # Construct BST
    root = constructBST(arr, 0, len(arr) - 1)

    # Create BinaryTree object and assign the constructed root
    bt = BinaryTree()
    bt.root = root

    # Print the tree
    bt.print()
