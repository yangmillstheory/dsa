def copy(g):
    m, n = len(g), len(g[0])
    _copy = [
        [None]*n
        for _ in range(m)
    ]
    for i in range(m):
        for j in range(n):
            _copy[i][j] = g[i][j]
    return _copy


def n_adj(g, i, j):
    m, n = len(g), len(g[0])
    s = 0
    for di, dj in [
        [-1, +1],
        [-1, -1],
        [-1, 0],
        [0, +1],
        [0, -1],
        [+1, +1],
        [+1, -1],
        [+1, 0],
    ]:
        if min(i+di, j+dj) >= 0 and i+di < m and j+dj < n and g[i+di][j+dj]:
            s += 1
    return s


class Solution(object):
    def gameOfLife(self, g):
        if not g or not g[0]:
            return
        h = copy(g)
        m, n = len(g), len(g[0])
        for i in range(m):
            for j in range(n):
                s = n_adj(h, i, j)
                if h[i][j]:
                    if s < 2 or s > 3:
                        g[i][j] = 0
                elif s == 3:
                    g[i][j] = 1
