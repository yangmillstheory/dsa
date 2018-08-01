def n_adj(g, i, j):
    m, n = len(g), len(g[0])
    s = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if (di or dj) and min(i+di, j+dj) >= 0 and i+di < m and j+dj < n and g[i+di][j+dj] in {1, 3}:
                s += 1
    return s


class Solution(object):
    def _game_of_life_optimized(self, g):
        # T(m, n) = O(m*n) (2 passes)
        # S(m, n) = O(1)
        if not g or not g[0]:
            return
        m, n = len(g), len(g[0])
        for i in range(m):
            for j in range(n):
                s = n_adj(g, i, j)
                if g[i][j] == 1 and 1 < n < 4:
                    g[i][j] += 2
                elif s == 3:
                    g[i][j] += 2
        for i in range(m):
            for j in range(n):
                g[i][j] = 1 if g[i][j] > 1 else 0

    def gameOfLife(self, g):
        return self._game_of_life_optimized(g)
