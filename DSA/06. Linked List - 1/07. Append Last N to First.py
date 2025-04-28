
# Problem statement

""" You have been given a singly linked list of integers along with an integer 'N'. Write a function to append the last
'N' nodes towards the front of the singly linked list and returns the new head to the list.

Hint:
Identify how many pointers you require and try traversing them to right places and connect nodes accordingly also don't
forget to disconnect what'scratch_KNN.py required else it could create cycles. """


# solution


from node_class import LinkedList


def eliminateDuplicates(head):
    """
    Removes duplicate nodes from a sorted linked list.
    Parameters:
        head (Node): The head node of the sorted linked list.
    Returns:
        Node: The head of the updated linked list without duplicates.
    """
    current = head

    # Traverse the linked list
    while current and current.next:
        if current.data == current.next.data:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            # Move to the next distinct node
            current = current.next

    return head


if __name__ == "__main__":
    # Create an instance of the LinkedList class
    ll = LinkedList()

    # Take user input to create the linked list
    ll.input()

    # Print the original linked list
    ll.print()

    # Eliminate duplicates from the linked list
    ll.head = eliminateDuplicates(ll.head)

    # Print the updated linked list
    ll.print()
