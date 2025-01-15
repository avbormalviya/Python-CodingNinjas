# Problem statement
""" Implement the BST class which includes following functions -

1. insert -
Given an element, insert that element in the BST at the correct position. If element is equal to the data of the node,
insert it in the left subtree.

2. search
Given an element, find if that is present in BST or not. Return true or false.

3. delete -
Given an element, remove that element from the BST. If the element which is to be deleted has both children,
replace that with the minimum element from right sub-tree.

4. printTree (recursive) -
Print the BST in in the following format -

For printing a node with data N, you need to follow the exact format -

N:L:x,R:y
where, N is data of any node present in the binary tree. x and y are the values of left and right child of node N.
Print the children only if it is not null.

There is no space in between.

You need to print all nodes in the recursive format in different lines. """

# Solution


from binary_tree import Node


class BST:
    def __init__(self):
        self.root = None

    def findMin(self, root):
        """
        Finds the minimum value in the subtree rooted at 'root'.

        Args:
            root (Node): Root of the subtree.

        Returns:
            int: The minimum value in the subtree, or None if the subtree is empty.
        """
        if root is None:
            return None

        while root.left:
            root = root.left
        return root.data

    def insertHelper(self, root, data):
        """
        Helper function to recursively insert data into the BST.

        Args:
            root (Node): Current root of the subtree.
            data (int): Data to insert.

        Returns:
            Node: Updated root of the subtree.
        """
        if root is None:
            return Node(data)

        if root.data == data:
            return root  # Ignore duplicates
        if root.data > data:
            root.left = self.insertHelper(root.left, data)
        else:
            root.right = self.insertHelper(root.right, data)

        return root

    def insert(self, data):
        """
        Inserts a value into the BST.

        Args:
            data (int): Value to insert.
        """
        self.root = self.insertHelper(self.root, data)

    def searchHelper(self, root, data):
        """
        Helper function to search for a value in the BST.

        Args:
            root (Node): Current root of the subtree.
            data (int): Value to search for.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        if root is None:
            return False

        if root.data == data:
            return True

        if root.data > data:
            return self.searchHelper(root.left, data)
        else:
            return self.searchHelper(root.right, data)

    def search(self, data):
        """
        Searches for a value in the BST.

        Args:
            data (int): Value to search for.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        return self.searchHelper(self.root, data)

    def deleteHelper(self, root, data):
        """
        Helper function to delete a value from the BST.

        Args:
            root (Node): Current root of the subtree.
            data (int): Value to delete.

        Returns:
            tuple: (Updated root of the subtree, bool indicating if deletion occurred).
        """
        if root is None:
            return None, False

        if root.data == data:
            # Case 1: No children
            if root.left is None and root.right is None:
                return None, True

            # Case 2: One child
            if root.left is None:
                return root.right, True
            if root.right is None:
                return root.left, True

            # Case 3: Two children
            minData = self.findMin(root.right)
            root.data = minData
            root.right, _ = self.deleteHelper(root.right, minData)
            return root, True

        elif root.data > data:
            root.left, deleted = self.deleteHelper(root.left, data)
            return root, deleted
        else:
            root.right, deleted = self.deleteHelper(root.right, data)
            return root, deleted

    def delete(self, data):
        """
        Deletes a value from the BST.

        Args:
            data (int): Value to delete.
        """
        self.root, _ = self.deleteHelper(self.root, data)

    def printTree(self, root):
        """
        Prints the BST in the required format.

        Args:
            root (Node): Root of the BST.
        """
        if root is None:
            return

        print(str(root.data), end='')

        if root.left is not None:
            print(f':L:{root.left.data}', end='')
        if root.right is not None:
            print(f',R:{root.right.data}', end='')
        print()

        self.printTree(root.left)
        self.printTree(root.right)


if __name__ == "__main__":
    bst = BST()

    # Inserting values into the BST
    values = [10, 5, 20, 7, 3, 15, 30, 2, 4, 6, 8, 14, 17, 25, 35, 1, 18, 40]
    for value in values:
        bst.insert(value)

    bst.printTree(bst.root)

    # Searching for values in the BST
    for search_value in [10, 20, 15, 30, 35, 40, 100]:
        print(bst.search(search_value))

    # Deleting values from the BST
    for delete_value in [10, 5, 20, 7, 3, 15, 30, 2, 4, 6, 8, 14, 17, 25, 35, 1, 18, 40]:
        bst.delete(delete_value)

    bst.printTree(bst.root)
