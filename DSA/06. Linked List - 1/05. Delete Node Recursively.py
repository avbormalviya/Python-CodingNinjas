
# Problem statement

""" Given a singly linked list of integers and position 'i', delete the node present at the 'i-th' position in the linked list recursively.

 Note :
Assume that the Indexing for the linked list always starts from 0.

No need to print the list, it has already been taken care. Only return the new head to the list. """


# solution


# Import the LinkedList class from the node_class module
from node_class import LinkedList


def deleteNode(head, pos, n):
    """
    Recursively deletes a node at a given position in the linked list.
    Parameters:
        head (Node): The head node of the linked list.
        pos (int): The 0-based position of the node to delete.
        n (int): The current length of the linked list.
    Returns:
        Node: The updated head of the linked list.
    """
    if not head:  # Base case: If the list is empty, return None
        return None

    if pos < 0 or pos >= n:  # Check for invalid position
        print("Invalid position.")
        return head

    if pos == 0:  # If the position is 0, delete the head node
        return head.next

    # Recursive case: Move to the next node and adjust the links
    head.next = deleteNode(head.next, pos - 1, n)

    return head


if __name__ == "__main__":
    # Create an instance of the LinkedList class
    ll = LinkedList()

    # Take user input to create the linked list
    ll.input()

    # Print the linked list
    ll.print()

    # Take user input for the position of the node to delete
    pos = int(input())

    # Delete the node and update the head of the linked list
    ll.head = deleteNode(ll.head, pos, ll.length)

    # Update the length of the linked list after deletion
    if 0 <= pos < ll.length:
        ll.length -= 1

    # Print the updated linked list
    ll.print()
