from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue) :
    if inputQueue.qsize() == 1:
        return

    top = inputQueue.get()

    reverseQueue(inputQueue)

    inputQueue.put(top)