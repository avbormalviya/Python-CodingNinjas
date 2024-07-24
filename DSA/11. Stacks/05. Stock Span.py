from sys import stdin


def stockSpan(price, n):
    stack = [0]
    ans = [1] * len(price)

    for i in range(1, n):
        while stack and price[stack[len(stack) - 1]] < price[i]:
            stack.pop()

        if not stack:
            ans[i] = i + 1
        else:
            ans[i] = i - stack[len(stack) - 1]

        stack.append(i)

    return ans


'''-------------- Utility Functions --------------'''


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

    print()


def takeInput():
    size = int(stdin.readline().strip())

    if size == 0:
        return list(), 0

    price = list(map(int, stdin.readline().strip().split(" ")))

    return price, size


# main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
