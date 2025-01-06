# Node class represents each node in the linked list
class Node:
    def __init__(self, data):
        # Initialize a node with the given data and set next to None
        self.data = data
        self.next = None


# LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        # Initialize the linked list with head, tail, and length
        self.head = None
        self.tail = None
        self.length = 0

    def input(self):
        """
        Takes space-separated integers from the user to create a linked list.
        Updates the head, tail, and length of the linked list.
        """
        input_list = list(map(int, input().split()))

        for data in input_list:
            # Create a new node for each input
            node = Node(data)

            if not self.head:  # If the list is empty, initialize the head
                self.head = node
            else:  # Otherwise, link the new node to the current tail
                self.tail.next = node

            self.tail = node  # Update the tail to the newly added node
            self.length += 1  # Increment the length

    def print(self):
        """
        Prints the linked list in the format: data1 -> data2 -> ... -> dataN.
        If the list is empty, it prints an appropriate message.
        """
        if not self.head:  # Check if the list is empty
            print("The linked list is empty.")
            return

        current = self.head  # Use a temporary pointer to traverse the list

        while current.next:
            print(current.data, end=" -> ")  # Print the data with an arrow
            current = current.next  # Move to the next node

        print(current.data)  # Print the last node's data without the arrow
