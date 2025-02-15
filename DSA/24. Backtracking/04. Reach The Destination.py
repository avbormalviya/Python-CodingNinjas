
# Problem statement

""" Given a source point (sx, sy) and a destination point (dx, dy), the task is to check if it is
possible to reach the destination point using the following valid moves:
(a, b) -> (a + b, b)
(a, b) -> (a, a + b)

Your task is to find if it is possible to reach the destination point using only the desired moves or not.

For example:
For the coordinates, source point = (1, 1) and destination point = (3, 5)
The output will be true as the destination point can be reached using the following sequence of moves:
(1, 1) -> (1, 2) -> (3, 2) -> (3, 5) """


# Solution


def can_reach_destination(sx, sy, dx, dy):
    while dx >= sx and dy >= sy:
        if dx == sx and dy == sy:
            return True  # We reached the starting point

        if dx > dy:
            if dy > sy:
                dx %= dy  # Reduce dx in steps of dy
            else:
                return (dx - sx) % dy == 0  # Check if (dx - sx) is a multiple of dy
        else:
            if dx > sx:
                dy %= dx  # Reduce dy in steps of dx
            else:
                return (dy - sy) % dx == 0  # Check if (dy - sy) is a multiple of dx

    return False  # If we go below (sx, sy), return False


sx, sy, dx, dy = map(int, input().split())
print(can_reach_destination(sx, sy, dx, dy))
