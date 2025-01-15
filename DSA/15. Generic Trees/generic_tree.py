import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


class GenericTree:
    def __init__(self):
        self.root = None

    def input(self):
        rootData = int(input("Enter root data: "))
        self.root = Node(rootData)

        q = queue.Queue()
        q.put(self.root)

        while not q.empty():
            curr = q.get()

            # Input children for the current node
            childData = input(f"Enter children of {curr.data} : ").strip()
            if childData:
                childrens = list(map(int, childData.split()))

                for child in childrens:
                    childNode = Node(child)
                    curr.children.append(childNode)
                    q.put(childNode)

    def print(self):
        if not self.root:
            print("Tree is empty!")
            return

        q = queue.Queue()
        q.put(self.root)

        while not q.empty():
            curr = q.get()
            print(f"{curr.data} : ", end="")
            for child in curr.children:
                print(f"{child.data}, ", end="")
                q.put(child)
            print()  # Move to the next line after printing children
