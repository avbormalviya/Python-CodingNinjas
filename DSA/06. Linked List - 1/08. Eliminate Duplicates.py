
# Problem statement

""" You have been given a singly linked list of integers where the elements are sorted in ascending order. Write a
function that removes the consecutive duplicate values such that the given list only contains unique elements and
returns the head to the updated list. """


# solution


from node_class import LinkedList


def eliminateDuplicates(head):
    current = head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head


if __name__ == "__main__":
    # Create an instance of the LinkedList class
    ll = LinkedList()

    # Take user input to create the linked list
    ll.input()

    # Print the linked list
    ll.print()

    # Eliminate duplicates and update the head of the linked list
    ll.head = eliminateDuplicates(ll.head)

    # Print the updated linked list
    ll.print()
