# Problem statement

""" Given a singly linked list of integers, reverse it using recursion and return the head to the modified list.
You have to do this in O(N) time complexity where N is the size of the linked list.

Note :
No need to print the list, it has already been taken care. Only return the new head to the list. """

# solution


from node_class import LinkedList


# Function to reverse a linked list recursively
def reverse(head):
    if head is None or head.next is None:  # Base case: if the list is empty or has one node
        return head

    # Recursive call to reverse the rest of the list
    new_head = reverse(head.next)

    # Reverse the direction of the current node's next pointer
    head.next.next = head
    head.next = None  # Break the link to prevent cycles

    return new_head  # Return the new head of the reversed list


if __name__ == '__main__':
    # Create a linked list and take input
    ll = LinkedList()
    ll.input()

    # Reverse the linked list and update its head
    ll.head = reverse(ll.head)

    # Print the reversed linked list
    ll.print()
