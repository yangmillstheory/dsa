class Solution(object):
    def transpose(self, g):
        if not g or not g[0]:
            return g
        m, n = len(g), len(g[0])
        res = [[None]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = g[i][j]
        return res
