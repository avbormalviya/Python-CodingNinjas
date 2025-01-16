
# Problem statement

""" Remove all leaf nodes from a given generic Tree. Leaf nodes are those nodes, which don't have any children.

Note : Root will also be a leaf node if it doesn't have any child. You don't need to print the tree, just remove
all leaf nodes and return the updated root. """


# Solution


from generic_tree import GenericTree


def removeLeafNodes(root):
    if not root:  # Base case: If the root is None, return None
        return None

    # Filter out the children that are leaf nodes
    root.children = [child for child in root.children if len(child.children) > 0]

    # Recursively process the remaining children
    for child in root.children:
        removeLeafNodes(child)

    return root


if __name__ == "__main__":
    tree = GenericTree()
    tree.input()  # Assuming GenericTree.input constructs the tree
    tree.root = removeLeafNodes(tree.root)
    tree.print()  # Assuming GenericTree.print prints the tree
