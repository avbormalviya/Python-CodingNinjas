
# Problem statement

""" A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time.
Implement a method to count how many possible ways the child can run up to the stairs. You need to return number
of possible ways W. """


# solution


def staircase(n):
    """
    Calculates the number of ways to climb a staircase with n steps
    using recursion. You can take 1, 2, or 3 steps at a time.

    Parameters:
    n (int): The total number of steps.

    Returns:
    int: The number of ways to climb the staircase.
    """
    # Base cases
    if n < 0:  # No way to climb negative steps
        return 0
    if n == 0:  # One way to stay at ground level
        return 1

    # Recursive case: sum of ways to reach the last 1, 2, and 3 steps
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


# Input: Number of steps
n = int(input())

# Output: Number of ways to climb
print(staircase(n))
