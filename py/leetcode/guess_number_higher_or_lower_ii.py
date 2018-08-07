class Solution(object):
    def getMoneyAmount(self, n):
        # T(n) = O(n^3)
        # S(n) = O(n^2)
        cache = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n, 0, -1):
            for j in range(1, n+1):
                if i >= j:
                    cache[i][j] = 0
                else:
                    cache[i][j] = min(
                       k+max(cache[i][k-1] if k-1 >= 0 else 0, cache[k+1][j] if k+1 <= n else 0)
                       for k in range(i, j+1)
                    )
        return cache[1][n]
