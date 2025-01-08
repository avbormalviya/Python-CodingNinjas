
# Problem statement

""" For a given singly linked list of integers, arrange the nodes such that all the even number nodes are placed after the all odd number nodes. The relative order of the odd and even terms should remain unchanged.

Note :
1. No need to print the linked list, it has already been taken care. Only return the new head to the list.
2. Don't create a new linked list.
3.  Just change the data, instead rearrange the provided list. """


# solution


from node_class import LinkedList


def evenAfterOdd(head):
    """
    Rearranges the linked list such that all odd-numbered nodes
    appear before all even-numbered nodes. The relative order of
    odd and even nodes is maintained by swapping data.

    Parameters:
        head (Node): The head node of the linked list.

    Returns:
        Node: The head of the rearranged linked list.
    """
    # Initialize pointers for traversing odd and even nodes
    odd = head
    even = head.next

    # Traverse the linked list until we reach the end
    while even and even.next:
        if odd.data % 2 != 0:  # Current odd node is in the correct position
            odd = odd.next
        elif even.data % 2 == 0:  # Current even node is in the correct position
            even = even.next
        else:
            # Swap data between the misplaced odd and even nodes
            odd.data, even.data = even.data, odd.data
            # Move both pointers to the next respective nodes
            odd = odd.next
            even = even.next

    return head


if __name__ == "__main__":
    # Create a LinkedList instance
    ll = LinkedList()

    # Take input for the linked list
    ll.input()

    # Rearrange the linked list
    ll.head = evenAfterOdd(ll.head)

    # Print the rearranged linked list
    ll.print()
