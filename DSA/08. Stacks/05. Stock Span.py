
# Problem statement

""" Amit has been working with an organization called 'Money Traders' for the past few years. The
organization is into the money trading business. His manager assigned him a task. For a given array/list
of stock'scratch_KNN.py prices for N days, find the stock'scratch_KNN.py span for each day.

The span of the stock'scratch_KNN.py price today is defined as the maximum number of consecutive days(starting from today
and going backwards) for which the price of the stock was less than today'scratch_KNN.py price.

Explanation:
For the stock prices [100, 80, 60, 70, 60, 75, 85], the span of each day is calculated by counting consecutive
previous days with a price less than or equal to today'scratch_KNN.py price:

Day 1 (100): No previous days, span = 1.
Day 2 (80): Less than 100, span = 1.
Day 3 (60): Less than 80, span = 1.
Day 4 (70): Greater than 60, span = 2.
Day 5 (60): Less than 70, span = 1.
Day 6 (75): Greater than 60, 70, and 60, span = 4.
Day 7 (85): Greater than all previous days, span = 6.
Final spans: [1, 1, 1, 2, 1, 4, 6].

Amit has to return an array/list of spans corresponding to each day'scratch_KNN.py stock'scratch_KNN.py price. Help him to achieve the task. """


# solution


def stockSpan(price):
    # Stack to store indices of stock prices in descending order
    stack = []
    # List to store the span for each day, initialized to 0 for all days
    ans = [0] * len(price)

    # Loop through each day in the price list
    for i in range(len(price)):
        # Pop elements from the stack while the price at the top of the stack
        # is less than or equal to the current price
        while stack and price[stack[-1]] <= price[i]:
            stack.pop()

        # If the stack is empty, it means all previous prices are smaller,
        # so the span is the entire range up to the current day (i + 1)
        # Otherwise, the span is the difference between the current index and the
        # index at the top of the stack
        ans[i] = i + 1 if not stack else i - stack[-1]

        # Push the current index onto the stack
        stack.append(i)

    # Return the list of spans
    return ans


# Input stock prices from the user as space-separated integers
price = list(map(int, input().split()))

# Call the stockSpan function and print the result
print(stockSpan(price))
