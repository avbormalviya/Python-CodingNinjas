
# Problem statement

""" Given a Singly Linked List of integers, delete all the alternate nodes in the list.

Example:
List: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> null
Alternate nodes will be:  20, 40, and 60.

Hence after deleting, the list will be:
Output: 10 -> 30 -> 50 -> null
Note :
The head of the list will remain the same. Don't need to print or return anything. """


# solution


from node_class import LinkedList


def deleteAlternateNodes(head):
    """
    Deletes every alternate node in the linked list starting from the second node.

    Args:
        head (Node): The head of the linked list.

    Returns:
        Node: The modified head of the linked list with alternate nodes removed.
    """
    current = head  # Start from the head of the list

    while current and current.next:  # Ensure there are at least two nodes to process
        current.next = current.next.next  # Skip the next node
        current = current.next  # Move to the next valid node

    return head


if __name__ == '__main__':
    # Create and input the linked list
    ll = LinkedList()
    ll.input()

    # Delete alternate nodes
    ll.head = deleteAlternateNodes(ll.head)

    # Print the modified linked list
    ll.print()
