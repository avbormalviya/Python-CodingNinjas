
# Problem statement

""" Given a singly linked list of integers, sort it using 'Merge Sort.'

Note :
No need to print the list, it has already been taken care. Only return the new head to the list. """


# solution


from node_class import LinkedList


def midPoint(head):
    """
    Finds the midpoint of the linked list.
    For an even-length list, it returns the first middle node.
    """
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next

    # Move slow one step and fast two steps until fast reaches the end
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def mergeTwoSortedLists(head1, head2):
    """
    Merges two sorted linked lists into a single sorted list.
    """
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    # Compare the data in head1 and head2 and recursively merge
    if head1.data < head2.data:
        head1.next = mergeTwoSortedLists(head1.next, head2)
        return head1
    else:
        head2.next = mergeTwoSortedLists(head1, head2.next)
        return head2


def mergeSort(head):
    """
    Sorts the linked list using merge sort.
    """
    if head is None or head.next is None:
        return head

    # Find the midpoint of the list
    mid = midPoint(head)
    left = head
    right = mid.next
    mid.next = None  # Split the list into two halves

    # Recursively sort both halves
    left = mergeSort(left)
    right = mergeSort(right)

    # Merge the sorted halves
    return mergeTwoSortedLists(left, right)


if __name__ == '__main__':
    # Create an instance of the linked list
    ll = LinkedList()

    # Take input for the linked list
    ll.input()

    # Perform merge sort on the linked list
    ll.head = mergeSort(ll.head)

    # Print the sorted linked list
    ll.print()
