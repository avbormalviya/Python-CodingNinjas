
# Problem statement

""" Given a large number represented in the form of a linked list. Write code to increment the number by 1 in-place
(i.e. without using extra space).

Note: You don't need to print the elements, just update the elements and return the head of updated LL.

Input Constraints: 1 <= Length of Linked List <=10^6. """


# solution

from node_class import LinkedList, Node  # Assuming `Node` is a class used in `LinkedList`


def nextNumber(head):
    """
    Increment the number represented by a linked list by 1.

    Args:
        head (Node): The head of the linked list representing the number.

    Returns:
        Node: The head of the new linked list after incrementing the number.
    """

    # Reverse the linked list to make addition easier
    def reverse(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    head = reverse(head)  # Reverse the linked list to process from least significant digit
    carry = 1  # Initialize carry as 1 (for adding 1)
    current = head

    # Traverse and add the carry
    while current:
        current.data += carry
        carry = current.data // 10
        current.data %= 10

        # If there'scratch_KNN.py no carry left, we can stop early
        if carry == 0:
            break

        # If it'scratch_KNN.py the last node and carry is still there, create a new node
        if not current.next and carry:
            current.next = Node(carry)
            carry = 0

        current = current.next

    # Reverse the list back to the original order
    head = reverse(head)
    return head


if __name__ == "__main__":
    ll = LinkedList()
    ll.input()  # Assuming input takes space-separated integers
    ll.head = nextNumber(ll.head)
    ll.print()
