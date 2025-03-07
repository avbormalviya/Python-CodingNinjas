
# Problem statement

""" Given a maze in the form of a binary rectangular matrix of size M*N, where each element can either be 0 or 1,
the task is to find the length of the shortest path in a maze from a given source cell to a destination cell.
The path can only be created out of a cell if its value is 1 and at any given moment, we can only move one step in
one of the four directions. The valid moves are:
Up: (x, y) -> (x - 1, y)
Left: (x, y) -> (x, y - 1)
Down: (x, y) -> (x + 1, y)
Right: (x, y) -> (x, y + 1)

If there is no path from a given source cell to a destination cell, return -1. """


# Solution


import heapq

# Possible 4-direction moves: Up, Right, Down, Left
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def shortest_path(maze, start, end):
    """
    Finds the shortest path in a maze using Dijkstra's algorithm.

    Parameters:
    maze (list of lists): 2D grid (1 = open path, 0 = wall).
    start (tuple): Starting coordinates (row, col).
    end (tuple): Target coordinates (row, col).

    Returns:
    int: Minimum steps to reach end, or -1 if unreachable.
    """
    n, m = len(maze), len(maze[0])

    # Distance array, initialize with infinity
    minCost = [[float('inf')] * m for _ in range(n)]
    minCost[start[0]][start[1]] = 0  # Starting position cost is 0

    minHeap = [(0, start)]  # (cost, (x, y))

    while minHeap:
        cost, (x, y) = heapq.heappop(minHeap)

        # If we reached the destination, return the cost
        if (x, y) == end:
            return cost

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            # Check if the move is within bounds and not a wall
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                new_cost = cost + 1

                # If we find a shorter path, update and push to heap
                if new_cost < minCost[nx][ny]:
                    minCost[nx][ny] = new_cost
                    heapq.heappush(minHeap, (new_cost, (nx, ny)))

    return -1  # Return -1 if there is no path


# Input Handling
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

# Compute shortest path
print(shortest_path(maze, start, end))
