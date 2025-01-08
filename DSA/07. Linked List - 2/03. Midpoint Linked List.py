
# Problem statement

""" For a given singly linked list of integers, find and return the node present at the middle of the list.

Note :
If the length of the singly linked list is even, then return the first middle node.

Example: Consider, 10 -> 20 -> 30 -> 40 is the given list, then the nodes present at the middle with respective data
values are, 20 and 30. We return the first node with data 20. """


# solution


from node_class import LinkedList


def midPoint(head):
    """
    Finds the midpoint of a linked list.
    Parameters:
        head (Node): The head of the linked list.
    Returns:
        int: The data at the midpoint node.
    """
    slow = head  # Slow pointer moves one step at a time
    fast = head.next  # Fast pointer moves two steps at a time

    # Traverse the list until the fast pointer reaches the end
    while fast and fast.next:
        slow = slow.next  # Move slow pointer one step
        fast = fast.next.next  # Move fast pointer two steps

    return slow.data  # Slow pointer will be at the midpoint


if __name__ == "__main__":
    ll = LinkedList()
    ll.input()
    print(midPoint(ll.head))
