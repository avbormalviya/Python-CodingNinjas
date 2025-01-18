
# Problem statement

""" You have been given a binary tree of integers.

Your task is to check if it is a binary heap tree or not.

Note:
A binary tree is a tree in which each parent node has at most two children.
A binary heap tree has the following properties.

1. It must be a complete binary tree. In the complete binary tree every level, except the last level,
is completely filled and the last level is as far left as possible.
2. Every parent must be greater than its all children nodes. """


# Solution


from binary_tree import BinaryTree


def isHeap(root):
    """
    Checks whether the given binary tree satisfies the heap property and is a complete binary tree.
    :param root: Node - Root node of the binary tree
    :return: bool - True if the tree is a heap, False otherwise
    """
    if not root:
        return True  # An empty tree is a valid heap

    # Use a queue for level-order traversal
    queue = [(root, 1)]
    i = 0

    while i < len(queue):
        node, index = queue[i]
        i += 1

        # Check left child
        if node.left:
            if node.left.data > node.data:
                return False  # Heap property violated
            queue.append((node.left, 2 * index))
        else:
            # If a left child is missing, all subsequent nodes should not have children
            break

        # Check right child
        if node.right:
            if node.right.data > node.data:
                return False  # Heap property violated
            queue.append((node.right, 2 * index + 1))
        else:
            # If a right child is missing, all subsequent nodes should not have children
            break

    # Ensure no nodes after a missing child
    while i < len(queue):
        node, index = queue[i]
        if node.left or node.right:
            return False  # Non-complete binary tree detected
        i += 1

    return True


# BinaryTree class should define a method to create a tree from input
bt = BinaryTree()
bt.input()  # Take input for the binary tree

# Check if the binary tree is a heap
print(isHeap(bt.root))
