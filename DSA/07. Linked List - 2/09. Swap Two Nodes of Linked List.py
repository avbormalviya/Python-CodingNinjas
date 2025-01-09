
# Problem statement

""" You have been given a singly linked list of integers along with two integers, 'i,' and 'j.' Swap the nodes that are present at the 'i-th' and 'j-th' positions and return the new head to the list.

Note :
1. Remember, You need to swap the nodes, not only the data.
2. Indexing starts from 0.
3. No need to print the list, it has already been taken care. """


# solution


from node_class import LinkedList


def swapNodes(head, i, j):
    """
    Swaps nodes at positions i and j in the linked list.

    Parameters:
        head (Node): The head of the linked list.
        i (int): Position of the first node to swap (0-based index).
        j (int): Position of the second node to swap (0-based index).

    Returns:
        Node: The head of the modified linked list.
    """
    # If both positions are the same, no swap needed
    if i == j:
        return head

    # Ensure i is less than j for simplicity
    if i > j:
        i, j = j, i

    # Initialize pointers for the nodes and their previous nodes
    prev1 = None
    curr1 = head
    prev2 = None
    curr2 = head

    # Traverse to the ith node
    for _ in range(i):
        prev1 = curr1
        curr1 = curr1.next

    # Traverse to the jth node
    for _ in range(j):
        prev2 = curr2
        curr2 = curr2.next

    # Handle swapping when one of the nodes is the head
    if prev1 is None:  # i is 0; curr1 is the head
        head = curr2
    else:
        prev1.next = curr2

    if prev2 is None:  # j is 0; curr2 is the head
        head = curr1
    else:
        prev2.next = curr1

    # Swap the next pointers of curr1 and curr2
    curr2.next, curr1.next = curr1.next, curr2.next

    return head


if __name__ == "__main__":
    # Create a linked list and take input
    ll = LinkedList()
    ll.input()

    # Take input for the indices to swap
    i = int(input())
    j = int(input())

    # Perform the swap and print the updated linked list
    ll.head = swapNodes(ll.head, i, j)
    ll.print()
