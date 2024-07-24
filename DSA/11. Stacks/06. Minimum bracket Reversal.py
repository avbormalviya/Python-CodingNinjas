from sys import stdin


def countBracketReversals(inputString):
    if len(inputString) % 2 != 0:
        return -1

    stack = []

    count = 0

    for i in inputString:
        if i in '([{':
            stack.append(i)

        elif i in ')]}':
            if not stack:
                stack.append(i)
                continue

            top = stack.pop()

            if (i == ')' and top != '(') or (i == ']' and top != '[') or (i == '}' and top != '{'):
                stack.append(top)
                stack.append(i)

    while stack:
        c1 = stack.pop()
        c2 = stack.pop()

        if c1 == c2:
            count += 1

        elif c1 == '{' and c2 == '}':
            count += 2

    return count


# main
print(countBracketReversals(stdin.readline().strip()))
