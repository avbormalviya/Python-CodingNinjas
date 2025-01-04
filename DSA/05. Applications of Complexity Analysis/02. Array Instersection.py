
# Problem statement

""" You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively. You need to print their
intersection; An intersection for this problem can be defined when both the arrays/lists contain a particular value or
to put it in other words, when there is a common value that exists in both the arrays/lists.

Note :
Input arrays/lists can contain duplicate elements.

The intersection elements printed would be in ascending order. """


# solution


from collections import Counter


# Function to find the intersection of two arrays
def arrayIntersection(arr1, arr2, n, m):
    # Create counters to store the frequency of elements in both arrays
    counter1 = Counter(arr1)  # Counter for arr1
    counter2 = Counter(arr2)  # Counter for arr2

    # Find the intersection of the two counters using the & operator
    # This gives a Counter of common elements with their minimum counts
    intersection = list(counter1 & counter2)

    # Sort the intersection to ensure the result is in ascending order
    intersection.sort()

    # Return the sorted intersection list
    return intersection


# Input: size of the first array (n), first array (arr1)
n = int(input())  # Read the size of the first array
arr1 = list(map(int, input().split()))  # Read the first array

# Input: size of the second array (m), second array (arr2)
m = int(input())  # Read the size of the second array
arr2 = list(map(int, input().split()))  # Read the second array

# Output: Print the sorted intersection of arr1 and arr2
print(arrayIntersection(arr1, arr2, n, m))

