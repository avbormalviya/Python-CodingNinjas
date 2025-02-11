
# Problem statement

""" You are given an sorted integer array of size 'n'.

Your task is to find and return all the unique subsets of the input array.

Subsets are arrays of length varying from 0 to 'n', that contain elements of the array.
But the order of elements should remain the same as in the input array.

Note:
The order of subsets is not important. You can return the subsets in any order. However, in the output,
you will see the subsets in lexicographically sorted order """


# Solution


def uniqueSubsets(arr, n):
    if n == 0:
        return [[]]




n = int(input())
arr = list(map(int, input().split()))

print(*uniqueSubsets(arr, n), sep="\n")
