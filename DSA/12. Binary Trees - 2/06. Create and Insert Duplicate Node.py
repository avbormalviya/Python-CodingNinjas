
# Problem statement

""" For a given a Binary Tree of type integer, duplicate every node of the tree and attach it to the left of itself.

The root will remain the same. So you just need to insert nodes in the given Binary Tree. """


# Solution


from binary_tree import BinaryTree, Node


def insertDuplicateNode(root):
    """
    Inserts a duplicate node for each node in the binary tree. The duplicate node is added
    as the left child of the original node.

    Args:
        root (Node): The root of the binary tree.

    Returns:
        Node: The updated root of the binary tree with duplicate nodes inserted.
    """
    if root is None:
        return

    # Recursively process the left and right subtrees
    insertDuplicateNode(root.left)
    insertDuplicateNode(root.right)

    # Create a duplicate node and insert it as the left child
    newNode = Node(root.data)
    newNode.left = root.left
    root.left = newNode


if __name__ == '__main__':
    # Input the tree
    tree = BinaryTree()
    root = tree.input()

    # Insert duplicate nodes
    insertDuplicateNode(root)

    # Print the updated tree
    tree.print()
