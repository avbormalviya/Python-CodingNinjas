
# Problem statement

""" You are given a generic tree. You have to replace each node with its depth value. You just have to update the
data of each node, there is no need to return or print anything. """


# Solution


from generic_tree import GenericTree, Node


def replaceWithDepth(root, depth=0):
    """
    Replaces the data of each node in the tree with its depth.

    Args:
        root (Node): The root node of the tree.
        depth (int): The depth of the current node. Defaults to 0 for the root node.
    """
    if root is None:
        return

    # Set the node's data to the current depth
    root.data = depth

    # Recursively process each child, incrementing the depth
    for child in root.children:
        replaceWithDepth(child, depth + 1)


if __name__ == "__main__":
    gt = GenericTree()
    gt.input()

    # Replace nodes with their respective depth values
    replaceWithDepth(gt.root)

    # Print the updated tree
    gt.print()

