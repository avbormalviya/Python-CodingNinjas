
# Problem statement

""" Ninja is planning to make dessert. For which he is going to buy ingredients. There are ‘N’ base flavors and ‘M’ toppings. Ninja has a target that he will be needing an amount of ‘K’ for making the dessert.

For making dessert, there are some basic rules

1. There should be exactly one base flavor.
2. Toppings can be one or more or none.
3. There are at most two toppings of each type.
Ninja wants to make a dessert with a total cost as close to the target price as possible.

You will be given an array/list flavor of size N representing the cost of each base flavor and another array/list
toppings of size 'M' representing the cost of each topping and the target price.

Your task is to help Ninja to find the closest possible cost of the dessert to the target price 'K'.
If there are multiple answers, return the lower one.

Example

Let N = 2 , M = 2 , K = 10, FLAVOR = [1,7] , TOPPING = [3, 4] , K = 10

Here we can make a dessert with the base flavor of price 7 and adding 1 topping of price 3. Which will cost 7 + 3 = 10,
which is exactly equal to k, so the closest possible price would be 10. """


# Solution


def closestCost(flavor, toppings, target):
    closest = float('inf')

    def dfs(index, current_cost):
        nonlocal closest

        # Update closest cost if the new one is better
        if abs(current_cost - target) < abs(closest - target) or \
                (abs(current_cost - target) == abs(closest - target) and current_cost < closest):
            closest = current_cost

        # If the current cost exceeds target, no need to explore further
        if current_cost >= target or index >= len(toppings):
            return

        # Explore options: (0, 1, or 2 of the current topping)
        dfs(index + 1, current_cost)  # 0 times
        dfs(index + 1, current_cost + toppings[index])  # 1 time
        dfs(index + 1, current_cost + 2 * toppings[index])  # 2 times

    # Try each base flavor and explore topping combinations
    for base in flavor:
        dfs(0, base)

    return closest


N = int(input())
M = int(input())
K = int(input())
flavor = list(map(int, input().split()))
toppings = list(map(int, input().split()))

print(closestCost(flavor, toppings, K))
