# Problem statement

""" Print the following pattern

Pattern for N = 4

*000*000*
0*00*00*0
00*0*0*00
000***000

"""

# solution

# taking input

n = int(input())

start = 1
end = (n * 2) + 1

i = 1

# print to create pattern

while i <= n:
    j = 1

    while j <= (n * 2) + 1:
        if j == start or j == ((n * 2) + 2)//2 or j == end:
            print('*', end='')
        else:
            print(0, end='')

        j += 1

    print()
    i += 1
    start += 1
    end -= 1
