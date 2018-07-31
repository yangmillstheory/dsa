import collections

_mark = object()


class Solution(object):
    def flood_fill_o1_space(self, g, x, y, color):
        if not g or not g[0]:
            return g
        m, n = len(g), len(g[0])
        orig = g[x][y]

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
            g[i][j] = _mark
            q.extend(adj(g, i, j))
        for i in range(m):
            for j in range(n):
                if g[i][j] is _mark:
                    g[i][j] = color
        return g

    def floodFill(self, g, x, y, color):
        if not g or not g[0]:
            return g
        m, n = len(g), len(g[0])
        orig, seen = g[x][y], set()

        def adj(g, i, j):
            return [
                (i+di, j+dj)
                for di in range(-1, 2)
                for dj in range(-1, 2)
                if (di == 0 or dj == 0) and (di or dj) and
                min(i+di, j+dj) >= 0 and i+di < m and j+dj < n and
                g[i+di][j+dj] == orig and (i+di, j+dj) not in seen
            ]
        q = collections.deque([(x, y)])
        while q:
            i, j = q.popleft()
            g[i][j] = color
            seen.add((i, j))
            q.extend(adj(g, i, j))
        return g

