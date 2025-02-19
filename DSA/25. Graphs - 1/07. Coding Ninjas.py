
# Problem statement

""" Given a NxM matrix containing Uppercase English Alphabets only. Your task is to tell
if there is a path in the given matrix which makes the sentence “CODINGNINJA” .

There is a path from any cell to all its neighbouring cells. For a particular cell, neighbouring cells are
those cells that share an edge or a corner with the cell. """


# Solution


moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
word = ['C', 'O', 'D', 'I', 'N', 'G', 'N', 'I', 'N', 'J', 'A']


def DFS(matrix, n, m, i, visited):
    if i == len(word):
        return 1

    if matrix[n][m] != word[i] or visited[n][m]:
        return 0

    visited[n][m] = True

    for i in range(len(moves)):
        x = n + moves[i][0]
        y = m + moves[i][1]

        if DFS(matrix, x, y, i + 1, visited):
            return 1

    return 0


def isPath(matrix, n, m):
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == word[0]:
                if DFS(matrix, i, j, 0, visited):
                    return 1

    return 0


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
print(isPath(matrix, n, m))
