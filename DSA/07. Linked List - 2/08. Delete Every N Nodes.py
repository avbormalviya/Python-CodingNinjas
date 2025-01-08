
# Problem statement

""" You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' Traverse the linked list
such that you retain the 'M' nodes, then delete the next 'N' nodes. Continue the same until the end of the linked list.
Indexing starts from 1.

To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.

Note :
No need to print the list, it has already been taken care. Only return the new head to the list. You can return null
in case where all nodes will be deleted. """


# solution


from node_class import LinkedList


def deleteEveryNNodes(head, M, N):
    """
    Deletes N nodes after every M nodes in a linked list.

    Parameters:
        head (Node): The head of the linked list.
        M (int): Number of nodes to retain.
        N (int): Number of nodes to delete after M nodes.

    Returns:
        Node: The head of the modified linked list.
    """
    # Handle edge cases where the input is invalid or no operation is needed
    if head is None or M < 0 or N <= 0:
        return head

    if M == 0:
        return None

    current = head  # Pointer to traverse the list

    while current is not None:
        # Retain M nodes
        for _ in range(M - 1):
            if current is None:  # End of list reached
                return head
            current = current.next

        # `prev` marks the end of the retained nodes
        prev = current

        # Skip N nodes
        for _ in range(N + 1):
            if current is None:  # End of list reached
                break
            current = current.next

        # Link the retained nodes to the rest of the list
        if prev is not None:
            prev.next = current

    return head


if __name__ == '__main__':
    # Create and take input for the linked list
    ll = LinkedList()
    ll.input()

    # Call the function to delete every N nodes after M nodes
    ll.head = deleteEveryNNodes(ll.head, 0, 2)

    # Print the modified linked list
    ll.print()
