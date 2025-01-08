
# Problem statement

""" Given a singly linked list of integers, reverse it iteratively and return the head to the modified list.

Note :
No need to print the list, it has already been taken care. Only return the new head to the list. """


# solution


from node_class import LinkedList


# Function to reverse a linked list iteratively
def reverse(head):
    prev = None  # To keep track of the previous node

    while head:  # Traverse the list until the end
        next = head.next  # Save the next node
        head.next = prev  # Reverse the link to point to the previous node
        prev = head  # Move prev forward
        head = next  # Move head forward

    return prev  # Return the new head of the reversed linked list


if __name__ == '__main__':
    # Create a linked list and take input
    ll = LinkedList()
    ll.input()

    # Reverse the linked list and update its head
    ll.head = reverse(ll.head)

    # Print the reversed linked list
    ll.print()
