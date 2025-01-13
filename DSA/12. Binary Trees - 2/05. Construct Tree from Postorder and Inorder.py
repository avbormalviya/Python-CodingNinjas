
# Problem statement

""" For a given postorder and inorder traversal of a Binary Tree of type integer stored in an array/list, create the binary tree using the given two arrays/lists. You just need to construct the tree and return the root.

Note:
Assume that the Binary Tree contains only unique elements. """


# Solution


from binary_tree import BinaryTree, Node


def buildTreeFromPreIn(preorder, inorder):
    """
    Constructs a binary tree from the given preorder and inorder traversal lists.

    Args:
        preorder (list): List of nodes in preorder.
        inorder (list): List of nodes in inorder.

    Returns:
        Node: The root node of the constructed binary tree.
    """
    if not preorder or not inorder:
        return None

    rootData = preorder[0]
    newNode = Node(rootData)

    # Find the index of the root in the inorder list
    rootIndexInInorder = inorder.index(rootData)

    # Slice the inorder list into left and right subtrees
    leftInorder = inorder[:rootIndexInInorder]
    rightInorder = inorder[rootIndexInInorder + 1:]

    # Get the left and right subtrees from the preorder list
    lenLeftInorder = len(leftInorder)
    leftPreorder = preorder[1:lenLeftInorder + 1]
    rightPreorder = preorder[lenLeftInorder + 1:]

    # Recursively build the left and right subtrees
    leftChild = buildTreeFromPreIn(leftPreorder, leftInorder)
    rightChild = buildTreeFromPreIn(rightPreorder, rightInorder)

    # Attach the left and right children to the new node
    newNode.left = leftChild
    newNode.right = rightChild

    return newNode


if __name__ == '__main__':
    preorder = [1, 2, 4, 5, 8, 3, 6, 9, 7]
    inorder = [4, 2, 8, 5, 1, 6, 9, 3, 7]

    root = buildTreeFromPreIn(preorder, inorder)

    bt = BinaryTree()
    bt.root = root

    bt.print()
