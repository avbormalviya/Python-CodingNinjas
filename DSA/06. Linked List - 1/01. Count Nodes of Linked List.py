
# Problem statement

""" Given the head of a singly linked list of integers, find and return its length. """


# solution


# Import everything from the node_class module
from node_class import LinkedList


# Function to calculate the length of the linked list
def lengthOfLinkedList(head):
    """
    Returns the length of the linked list.
    If the list is empty, prints a message and returns 0.
    """
    if not head:  # Check if the linked list is empty
        print("The linked list is empty.")
        return 0

    count = 1  # Initialize count with 1 to include the head node

    while head.next:  # Traverse until the end of the list
        head = head.next  # Move to the next node
        count += 1  # Increment the count for each node

    return count


if __name__ == "__main__":
    # Create an instance of the LinkedList class
    ll = LinkedList()

    # Take user input to create the linked list
    ll.input()

    # Print the linked list
    ll.print()

    # Calculate and print the length of the linked list
    print(lengthOfLinkedList(ll.head))
