
# Problem statement

# Given a linked list, find and return the length of the given linked list recursively.


# solution


# Import the LinkedList class from the node_class module
from node_class import LinkedList


def lengthOfLinkedList(head):
    """
    Recursively calculates the length of the linked list.
    Parameters:
        head (Node): The head node of the linked list.
    Returns:
        int: The length of the linked list.
    """
    if not head:  # Base case: If the list is empty, return 0
        return 0

    # Recursive case: 1 (current node) + length of the rest of the list
    return 1 + lengthOfLinkedList(head.next)


if __name__ == "__main__":
    # Create an instance of the LinkedList class
    ll = LinkedList()

    # Take user input to create the linked list
    ll.input()

    # Print the linked list
    ll.print()

    # Calculate the length of the linked list using recursion
    length = lengthOfLinkedList(ll.head)

    # Print the calculated length
    print(length)
