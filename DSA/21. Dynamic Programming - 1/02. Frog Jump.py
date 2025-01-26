
# Problem statement

""" There is a frog on the '1st' step of an 'N' stairs long staircase. The frog wants to reach the 'Nth' stair.
'HEIGHT[i]' is the height of the '(i+1)th' stair.If Frog jumps from 'ith' to 'jth' stair, the energy lost in the
jump is given by absolute value of ( HEIGHT[i-1] - HEIGHT[j-1] ). If the Frog is on 'ith' staircase, he can jump either
to '(i+1)th' stair or to '(i+2)th' stair. Your task is to find the minimum total energy used by the frog to
reach from '1st' stair to 'Nth' stair.

For Example
If the given ‘HEIGHT’ array is [10,20,30,10], the answer 20 as the frog can jump from 1st stair to 2nd stair
(|20-10| = 10 energy lost) and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost). So, the total
energy lost is 20. """


# Solution


def frogJumpRecursive(height, n, idx, memo):
    # Base case: if at the first step, no cost is incurred
    if idx == 0:
        return 0

    # If the result is already computed, return it
    if memo[idx] != -1:
        return memo[idx]

    # Calculate the cost for one step
    one_step = frogJumpRecursive(height, n, idx - 1, memo) + abs(height[idx] - height[idx - 1])

    # Calculate the cost for two steps, if possible
    two_steps = float('inf')
    if idx > 1:
        two_steps = frogJumpRecursive(height, n, idx - 2, memo) + abs(height[idx] - height[idx - 2])

    # Store the result in memo and return
    memo[idx] = min(one_step, two_steps)
    return memo[idx]


def frogJump(height, n):
    # Initialize a memoization array
    memo = [-1] * n
    # Start from the last step
    return frogJumpRecursive(height, n, n - 1, memo)


# Input handling
n = int(input())
height = list(map(int, input().split()))
print(frogJump(height, n))
