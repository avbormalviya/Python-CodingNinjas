
# Problem statement

""" For a given a Binary Tree of type integer, print the complete information of every node, when traversed in a level-order fashion.

To print the information of a node with data D, you need to follow the exact format :

           D:L:X,R:Y

Where D is the data of a node present in the binary tree.
X and Y are the values of the left(L) and right(R) child of the node.
Print -1 if the child doesn't exist. """


# solution


from binary_tree import BinaryTree
import queue


def printLevelWise(root):
    """
    Prints the complete information of every node in a binary tree
    when traversed in a level-order fashion.

    Args:
        root: The root node of the binary tree.

    Returns:
        None
    """
    if root is None:
        return

    # Initialize a queue to store the nodes of the binary tree
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        # Get the current node from the front of the queue
        curr = q.get()

        # Print the information of the current node
        print(f"{curr.data}:", end="")

        # Print the left child of the current node
        if curr.left is not None:
            print(f"L:{curr.left.data},", end="")
            q.put(curr.left)
        else:
            print("L:-1,", end="")

        # Print the right child of the current node
        if curr.right is not None:
            print(f"R:{curr.right.data}", end="")
            q.put(curr.right)
        else:
            print("R:-1", end="")

        print()


if __name__ == '__main__':
    # Initialize a binary tree using the BinaryTree class
    tree = BinaryTree()

    # Build the binary tree based on user input
    tree.input()

    # Print the complete information of every node in the binary tree
    printLevelWise(tree.root)
