
# Problem statement

""" You have been given a head to a singly linked list of integers. Write a function check to whether the list given is
a 'Palindrome' or not. """


# solution


from node_class import LinkedList


def reverseLL(node):
    """
    Reverses a linked list recursively.
    Parameters:
        node (Node): The head node of the linked list.
    Returns:
        Node: The new head of the reversed linked list.
    """
    if not node or not node.next:  # Base case: empty list or single node
        return node

    # Recursive call to reverse the rest of the list
    new_head = reverseLL(node.next)

    # Adjust the pointers to reverse the direction
    node.next.next = node
    node.next = None  # Break the original link

    return new_head


def isPalindrome(head):
    """
    Checks if a linked list is a palindrome.
    Parameters:
        head (Node): The head node of the linked list.
    Returns:
        bool: True if the linked list is a palindrome, False otherwise.
    """
    if not head or not head.next:  # Empty or single-node list is always a palindrome
        return True

    # Find the middle of the list using slow and fast pointers
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the list
    reversed_second_half = reverseLL(slow)

    # Check palindrome by comparing the first and second halves
    first_half = head
    second_half = reversed_second_half
    is_palindrome = True

    while second_half:
        if first_half.data != second_half.data:
            is_palindrome = False
            break
        first_half = first_half.next
        second_half = second_half.next

    # Restore the second half of the list
    reverseLL(reversed_second_half)

    return is_palindrome


if __name__ == "__main__":
    ll = LinkedList()
    ll.input()
    print(isPalindrome(ll.head))
