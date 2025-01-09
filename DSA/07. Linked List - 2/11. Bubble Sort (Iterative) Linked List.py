
# Problem statement

""" Given a singly linked list of integers, sort it using 'Bubble Sort.'

Note :
No need to print the list, it has already been taken care. Only return the new head to the list. """


# solution


from node_class import LinkedList


def bubbleSort(head):
    """
    Sorts a linked list using the Bubble Sort algorithm.

    Parameters:
        head (Node): The head of the linked list.

    Returns:
        Node: The new head of the sorted linked list.
    """
    if not head or not head.next:  # Edge case: empty list or single node
        return head

    # Flag to check if any swaps are made
    swapped = True

    while swapped:
        swapped = False
        current = head
        prev = None

        # Traverse the list and perform pairwise comparisons
        while current and current.next:
            if current.data > current.next.data:
                # Swap nodes
                swapped = True

                if prev:  # If we're not at the head
                    temp = current.next
                    current.next = temp.next
                    temp.next = current
                    prev.next = temp
                    prev = temp
                else:  # Special case for swapping at the head
                    temp = current.next
                    current.next = temp.next
                    temp.next = current
                    head = temp
                    prev = temp
            else:
                # Move to the next pair
                prev = current
                current = current.next

    return head


if __name__ == '__main__':
    # Create the linked list and take input
    ll = LinkedList()
    ll.input()

    # Sort the linked list using Bubble Sort
    ll.head = bubbleSort(ll.head)

    # Print the sorted linked list
    ll.print()
