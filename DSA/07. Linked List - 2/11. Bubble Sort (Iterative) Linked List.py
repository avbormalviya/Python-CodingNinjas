
# Problem statement

""" Given a singly linked list of integers, sort it using 'Bubble Sort.'

Note :
No need to print the list, it has already been taken care. Only return the new head to the list. """


def bubbleSort(head):
    if head is None or head.next is None:
        return head

    current = head

    while current is not None and current.next is not None:
        if current.data > current.next.data:
            temp = current.data
            current.data = current.next.data
            current.next.data = temp
        current = current.next
