# Problem statement

""" Write a program to input marks of three tests of a student (all integers). Then calculate and print the average of all
test marks. """

# solution

# taking integer input

firstTestMark = int(input())
secondTestMark = int(input())
thirdTestMark = int(input())

# find average marks of three tests of a student

averageMarks = (firstTestMark + secondTestMark + thirdTestMark) / 3

# print average marks

print(averageMarks)