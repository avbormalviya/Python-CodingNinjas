
# Problem statement

""" You have been given two sorted(in ascending order) singly linked lists of integers.

Write a function to merge them in such a way that the resulting singly linked list is also sorted(in ascending order)
and return the new head to the list.

Note :
Try solving this in O(1) auxiliary space. """


# solution


from node_class import LinkedList


def mergeTwoSortedLinkedLists(head1, head2):
    """
    Merges two sorted linked lists into a single sorted linked list.
    Parameters:
        head1 (Node): The head of the first sorted linked list.
        head2 (Node): The head of the second sorted linked list.
    Returns:
        Node: The head of the merged sorted linked list.
    """
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # Initialize the new head for the merged list
    if head1.data < head2.data:
        new_head = head1
        head1 = head1.next
    else:
        new_head = head2
        head2 = head2.next

    # Use a pointer to track the current position in the merged list
    current = new_head

    # Traverse both lists until one is exhausted
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        # Move the pointer forward in the merged list
        current = current.next

    # Attach the remaining part of the non-exhausted list
    if head1:
        current.next = head1
    if head2:
        current.next = head2

    return new_head


if __name__ == '__main__':
    # Create two linked lists
    ll1 = LinkedList()
    ll2 = LinkedList()

    # Take input for both linked lists
    ll1.input()
    ll2.input()

    # Merge the two sorted linked lists
    ll1.head = mergeTwoSortedLinkedLists(ll1.head, ll2.head)

    # Print the merged linked list
    print()
    ll1.print()
