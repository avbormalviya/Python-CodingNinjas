
# Problem statement

""" You have been given two integer arrays/lists (ARR1 and ARR2) of size N and M, respectively. You need to print
their intersection; An intersection for this problem can be defined when both the arrays/lists contain a particular
value or to put it in other words, when there is a common value that exists in both the arrays/lists.

Note :
Input arrays/lists can contain duplicate elements.

The intersection elements printed would be in the order they appear in the second array/list (ARR2). """


# Solution


from collections import Counter


def printIntersection(arr1, arr2):
    """
    Prints the intersection of two arrays, considering the frequency of elements.
    Each element is printed as many times as it appears in both arrays.
    :param arr1: List[int] - The first array
    :param arr2: List[int] - The second array
    """
    # Count the frequency of elements in arr1
    count1 = Counter(arr1)

    # Iterate through arr2 to find common elements
    for num in arr2:
        if count1.get(num, 0) > 0:  # Check if the element exists in count1 with positive frequency
            print(num)  # Print the element
            count1[num] -= 1  # Decrement the frequency of the element in count1


# Read the input
n = int(input())  # Length of the first array
arr1 = list(map(int, input().split()))  # First array
m = int(input())  # Length of the second array
arr2 = list(map(int, input().split()))  # Second array

# Print the intersection
printIntersection(arr1, arr2)

