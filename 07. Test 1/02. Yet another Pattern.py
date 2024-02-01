# Problem statement

""" Ninja was playing with her sister to solve a puzzle pattern. However, even after taking several hours, they could
not solve the problem.

A value of N is given to them, and they are asked to solve the problem. Since they are stuck for a while, they ask
you to solve the problem. Can you help solve this problem?

Example : Pattern for N = 4

****
 ***
  **
   *

"""


# solution

def ninjaPuzzle(n):
    i = 1

    while i <= n:
        j = i - 1
        k = 1

        while j >= 1:
            print(' ', end='')

            j -= 1

        while k <= n - i + 1:
            print('*', end='')

            k += 1

        print()
        i += 1
