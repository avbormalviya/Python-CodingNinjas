
# Problem statement

""" For a given a singly linked list of integers and a position 'i', print the node data at the 'i-th' position.

Note :
1. Assume that the Indexing for the singly linked list always starts from 0.
2. If the given position 'i', is greater than the length of the given singly linked list, then don't print anything. """


# solution


# Import the LinkedList class from the node_class module
from node_class import LinkedList


# Function to print the i-th node data
def printIthNode(head, i):
    """
    Prints the data of the i-th node in the linked list.
    Parameters:
        head (Node): The head node of the linked list.
        i (int): The index (0-based) of the node whose data is to be printed.

    Returns:
        int: The data of the i-th node if it exists, otherwise None.
    """
    if not head:  # Check if the list is empty
        print("The linked list is empty.")
        return None

    current = head  # Use a temporary pointer to traverse the list

    for _ in range(i):  # Traverse the list i times
        if current:  # Check if the current node is not None
            current = current.next
        else:
            print(f"Index {i} is out of bounds.")
            return None

    if current:  # If the i-th node exists, return its data
        return current.data
    else:
        print(f"Index {i} is out of bounds.")
        return None


if __name__ == "__main__":
    # Create an instance of the LinkedList class
    ll = LinkedList()

    # Take user input to create the linked list
    ll.input()

    # Print the linked list
    ll.print()

    # Take user input for the index
    i = int(input())

    # Retrieve and print the i-th node's data
    data = printIthNode(ll.head, i)
    if data is not None:
        print(data)
