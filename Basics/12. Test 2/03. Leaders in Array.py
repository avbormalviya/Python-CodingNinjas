
# Problem statement

""" Given an integer array A of size n. Find and print all the leaders present in the input array. An array element
A[i] is called Leader, if all the elements following it (i.e. present at its right) are less than or equal to A[i].

Print all the leader elements separated by space and in the same order they are present in the input array. """


# solution


def leadersInArray(arr):
    # List to store leaders, initialized with the last element as it's always a leader
    leaders = []
    max_from_right = float('-inf')  # Initialize to negative infinity

    # Traverse the array from right to left
    for i in reversed(arr):
        if i >= max_from_right:
            leaders.append(i)  # Add current element as leader
            max_from_right = i  # Update max_from_right

    # Reverse the list of leaders to restore original order
    return leaders[::-1]


# Input the size of the array
n = int(input())

# Input the array elements
arr = list(map(int, input().split()))

# Print the leaders in the array
print(*leadersInArray(arr))
