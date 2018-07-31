import collections


class Solution(object):
    def floodFill(self, g, x, y, color):
        if not g or not g[0]:
            return g
        m, n = len(g), len(g[0])
        orig = g[x][y]
        if orig == color:
            return g

        def adj(g, i, j):
            return [
                (i+di, j+dj)
                for di in range(-1, 2)
                for dj in range(-1, 2)
                if (di == 0 or dj == 0) and (di or dj) and
                min(i+di, j+dj) >= 0 and i+di < m and j+dj < n and
                g[i+di][j+dj] == orig
            ]
        q = collections.deque([(x, y)])
        while q:
            i, j = q.popleft()
            g[i][j] = color
            q.extend(adj(g, i, j))
        return g
