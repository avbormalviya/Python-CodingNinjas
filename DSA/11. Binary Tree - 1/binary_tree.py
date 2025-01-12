import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Method to input the binary tree in level order
    def input(self):
        levelOrder = list(map(int, input().split()))
        start = 0

        # If the first element is -1, the tree is empty
        if levelOrder[start] == -1:
            return None

        root = Node(levelOrder[start])
        start += 1

        q = queue.Queue()
        q.put(root)

        while not q.empty():
            curr = q.get()

            # Process left child
            if start < len(levelOrder):
                leftChild = levelOrder[start]
                start += 1

                if leftChild != -1:
                    leftNode = Node(leftChild)
                    curr.left = leftNode
                    q.put(leftNode)

            # Process right child
            if start < len(levelOrder):
                rightChild = levelOrder[start]
                start += 1

                if rightChild != -1:
                    rightNode = Node(rightChild)
                    curr.right = rightNode
                    q.put(rightNode)

        self.root = root
        return root

