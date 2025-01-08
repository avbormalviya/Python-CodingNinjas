
# Problem statement

""" Given a singly linked list of integers and an integer n, find and return the index for the first occurrence of
'n' in the linked list. -1 otherwise.

Follow a recursive approach to solve this.

Note :
Assume that the Indexing for the linked list always starts from 0. """


# solution


from node_class import LinkedList


def findNode(head, n):
    """
    Finds the index of the node containing the value n in the linked list.
    Uses a recursive approach.

    Parameters:
        head (Node): The head of the linked list.
        n (int): The value to search for.

    Returns:
        int: The index of the node (0-based) if found, otherwise -1.
    """
    if head is None:  # Base case: Reached end of the list
        return -1

    if head.data == n:  # Base case: Value found
        return 0

    # Recursive call to check the rest of the list
    smallOutput = findNode(head.next, n)

    if smallOutput == -1:  # Value not found in the remaining list
        return -1

    return smallOutput + 1  # Increment the index for the current node


if __name__ == "__main__":
    # Create a linked list and take input
    ll = LinkedList()
    ll.input()

    # Take the value to search for
    value = int(input())

    # Find the index of the node and print the result
    print(findNode(ll.head, value))
