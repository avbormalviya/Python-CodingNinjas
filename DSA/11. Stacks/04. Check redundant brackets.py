
from sys import stdin

import queue

def checkRedundantBrackets(string) :
    stack = []

    for char in expression:
        if char == ')':
            top = stack.pop()
            found = False

            while top != '(':
                if top in {'+', '-', '*', '/'}:
                    found = True
                top = stack.pop()

            if not found:
                return True
        else:
            stack.append(char)

    return False




#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
