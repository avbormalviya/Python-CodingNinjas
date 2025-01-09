
# Problem statement

""" Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its
modified list.

 'k' is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not
 a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.

Example :
Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4

Note :
No need to print the list, it has already been taken care. Only return the new head to the list. """


# solution


from node_class import LinkedList


def reverse(head, k):
    """
    Reverses the first k nodes of a linked list.

    Parameters:
        head (Node): The head of the linked list.
        k (int): The number of nodes to reverse.

    Returns:
        Node: The new head of the linked list after reversing the first k nodes.
    """
    if head is None or k <= 0:
        return head

    curr = head
    prev = None
    count = 0

    # Reverse the first k nodes
    while curr and count < k:
        next_node = curr.next  # Save the next node
        curr.next = prev       # Reverse the current node's pointer
        prev = curr            # Move prev to the current node
        curr = next_node       # Move curr to the next node
        count += 1

    # Connect the remaining part of the list
    if head:  # At the end of the reversed segment, 'head' is the new tail
        head.next = curr

    # Return the new head of the list (prev is the head of the reversed segment)
    return prev


if __name__ == '__main__':
    # Create the linked list and take input
    ll = LinkedList()
    ll.input()

    # Input for k
    k = int(input())

    # Reverse the first k nodes and update the head
    ll.head = reverse(ll.head, k)

    # Print the updated linked list
    ll.print()
