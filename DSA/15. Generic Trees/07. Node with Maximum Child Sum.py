
# Problem statement

""" Given a generic tree, find and return the node for which sum of its data and data of all its child nodes is maximum.
In the sum, data of the node and data of its immediate child nodes has to be taken. """


# Solution


from generic_tree import GenericTree, Node


def maxSumNode(root):
    """
    Finds the node in a generic tree whose subtree (including itself) has the maximum sum of node values.

    Args:
        root (Node): The root node of the tree.

    Returns:
        Tuple[Node, int]: The node with the maximum subtree sum and the sum itself.
    """
    if root is None:
        return None, 0

    # Calculate the sum of the current node and its immediate children
    current_sum = root.data + sum(child.data for child in root.children)

    # Initialize max node and max sum with the current node
    max_node = root
    max_sum = current_sum

    # Recursively find the max sum in the children subtrees
    for child in root.children:
        child_max_node, child_max_sum = maxSumNode(child)

        # Update if a child'scratch_KNN.py subtree has a greater sum
        if child_max_sum > max_sum:
            max_node = child_max_node
            max_sum = child_max_sum

    return max_node, max_sum


if __name__ == "__main__":
    gt = GenericTree()
    gt.input()
    max_node, max_sum = maxSumNode(gt.root)
    print(max_node.data, max_sum)
