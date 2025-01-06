
# Problem statement

""" You have been given a singly linked list of integers. Write a function to print the list in a reverse order.

To explain it further, you need to start printing the data from the tail and move towards the head of the list,
printing the head data at the end.

Note :
You can’t change any of the pointers in the linked list, just print the linked list in the reverse order. """


# solution


from node_class import LinkedList


def print_reverse(head):
    """
    Recursively prints the linked list in reverse order.
    Parameters:
        head (Node): The head node of the linked list.
    """
    if not head:  # Base case: if the list is empty or end of the list is reached
        return

    print_reverse(head.next)  # Recursive call for the next node
    print(head.data, end=" ")  # Print the current node's data after recursive call


if __name__ == "__main__":
    # Create an instance of the LinkedList class
    ll = LinkedList()

    # Take user input to create the linked list
    ll.input()

    # Print the linked list in reverse order
    print_reverse(ll.head)
