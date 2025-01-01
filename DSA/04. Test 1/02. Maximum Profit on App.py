
# Problem statement

""" You have made a smartphone app and want to set its subscription price such that the profit earned is maximised.
There are certain users who will subscribe to your app only if their budget is greater than or equal to your price.

You will be provided with a list of size N having budgets of subscribers and you need to return the maximum profit
that you can earn.

Lets say you decide that price of your app is Rs. x and there are N number of subscribers. So maximum profit you
can earn is :
    Profit = m * x

where m is total number of subscribers whose budget is greater than or equal to x. """


# solution


def maxProfitRecursive(prices, curr, n):
    # Base case: No more items left to sell
    if curr == n:
        return 0

    # Recursive case:
    # Option 1: Skip the current item
    profit1 = maxProfitRecursive(prices, curr + 1, n)

    # Option 2: Sell the current item
    # The position multiplier is (n - curr) because it's sorted
    profit2 = prices[curr] * (n - curr)

    # Return the maximum profit
    return max(profit1, profit2)


def maxProfit(prices):
    prices.sort()  # Sort prices to maximize profit
    return maxProfitRecursive(prices, 0, len(prices))


# Input size of the array
n = int(input())

# Input array elements
arr = list(map(int, input().split()))

# Output result
print(maxProfit(arr))
