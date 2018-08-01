class Solution(object):
    def __init__(self):
        self.n = 0

    def islandPerimeter(self, g):
        if not g or not g[0]:
            return 0
        m, n = len(g), len(g[0])

        def adj(i, j):
            return [
                (i+di, j+dj)
                for di, dj in ((di, dj)
                    for di in range(-1, 2)
                    for dj in range(-1, 2)
                    if abs(di) != abs(dj) and i+di < m and j+dj < n and min(i+di, j+dj) >= 0)
            ]

        _visiting = 'X'

        def dfs(i, j):
            self.n += 4
            g[i][j] = _visiting
            for x, y in adj(i, j):
                if g[x][y] == 1:
                    self.n -= 1
                    dfs(x, y)
                elif g[x][y] == _visiting:
                    self.n -= 1
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    dfs(i, j)
        return self.n
