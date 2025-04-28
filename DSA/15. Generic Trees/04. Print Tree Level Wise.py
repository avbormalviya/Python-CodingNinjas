
# Problem statement

""" Given a generic tree, print the input tree in level wise order.

For printing a node with data N, you need to follow the exact format -

N:x1,x2,x3,...,xn

where, N is data of any node present in the generic tree. x1, x2, x3, ...., xn are the children of node N. Note that there is no space in between.
You need to print all nodes in the level order form in different lines. """


# Solution


import queue
from generic_tree import GenericTree


def printLevelWise(root):
    """
    Prints the generic tree level-wise.

    Args:
        root (Node): The root node of the tree.

    Returns:
        None
    """
    if not root:
        print("Tree is empty!")
        return

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        curr = q.get()

        # Print the current node'scratch_KNN.py data
        print(f"{curr.data} -> ", end="")

        # Collect and enqueue the children
        child_data = []
        for child in curr.children:
            child_data.append(str(child.data))
            q.put(child)

        # Print children data or a placeholder if none
        if child_data:
            print(", ".join(child_data))
        else:
            print("None")  # Indicates no children for the current node


if __name__ == "__main__":
    gt = GenericTree()
    gt.input()
    printLevelWise(gt.root)
