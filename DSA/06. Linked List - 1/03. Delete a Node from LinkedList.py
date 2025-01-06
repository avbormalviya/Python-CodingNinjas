# Problem statement

""" You have been given a linked list of integers. Your task is to write a function that deletes a node from a given position, 'POS'.

Note :
Assume that the Indexing for the linked list always starts from 0.

If the position is greater than or equal to the length of the linked list, you should return the same linked list
without any change."""


# solution


# Import the LinkedList class from the node_class module
from node_class import LinkedList


# Function to delete a node from a linked list at a given position
def deleteNode(head, pos, n):
    """
    Deletes a node from the linked list at the specified position.
    Parameters:
        head (Node): The head node of the linked list.
        pos (int): The 0-based position of the node to delete.
        n (int): The current length of the linked list.

    Returns:
        Node: The updated head of the linked list.
    """
    if not head:  # Check if the list is empty
        print("The linked list is empty.")
        return None

    if pos < 0 or pos >= n:  # Validate the position
        print("Invalid position.")
        return head

    if pos == 0:  # If the position is 0, delete the head node
        return head.next

    # Traverse the list to find the node before the target position
    current = head
    for _ in range(pos - 1):
        current = current.next

    # Update the next pointer to skip the target node
    current.next = current.next.next

    return head


if __name__ == "__main__":
    # Create an instance of the LinkedList class
    ll = LinkedList()

    # Take user input to create the linked list
    ll.input()

    # Take the position of the node to delete
    pos = int(input())

    # Delete the node and update the head of the linked list
    ll.head = deleteNode(ll.head, pos, ll.length)

    # Update the length of the linked list after deletion
    if 0 <= pos < ll.length:
        ll.length -= 1

    # Print the updated linked list
    ll.print()

