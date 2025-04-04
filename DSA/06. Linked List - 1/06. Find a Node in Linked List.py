
# Problem statement

""" You have been given a singly linked list of integers. Write a function that returns the index/position of integer data denoted by 'N' (if it exists). Return -1 otherwise.

Note :
Assume that the Indexing for the singly linked list always starts from 0. """


# solution

from node_class import LinkedList


def findNode(head, val):
    """
    Finds the first occurrence of a node with the given value in the linked list.
    Parameters:
        head (Node): The head node of the linked list.
        val (int): The value to search for in the linked list.
    Returns:
        int: The index of the first node containing the value, or -1 if not found.
    """
    if not head:  # Check if the list is empty
        print("The linked list is empty.")
        return -1

    index = 0

    # Traverse the linked list
    while head:
        if head.data == val:  # Check if the current node contains the value
            return index

        head = head.next  # Move to the next node
        index += 1

    # If the value is not found, return -1
    return -1


if __name__ == "__main__":
    # Create an instance of the LinkedList class
    ll = LinkedList()

    # Take user input to create the linked list
    ll.input()

    # Print the linked list
    ll.print()

    # Take user input for the value to search
    val = int(input())

    # Find the index of the node with the given value
    index = findNode(ll.head, val)

    # Print the result
    print(index)
