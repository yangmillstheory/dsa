class Solution(object):
    def imageSmoother(self, g):
        # T(m, n) = O(m*n)
        # S(m, n) = O(1)
        m, n = len(g), len(g[0])

        def smoothify(g, i, j):
            c = smoothness = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if min(x, y) < 0 or x >= m or y >= n:
                        continue
                    c += 1
                    if isinstance(g[x][y], tuple):
                        smoothness += g[x][y][0]
                    else:
                        smoothness += g[x][y]
            g[i][j] = g[i][j], smoothness//c
        for i in range(m):
            for j in range(n):
                smoothify(g, i, j)
        for i in range(m):
            for j in range(n):
                g[i][j] = g[i][j][1]
        return g
