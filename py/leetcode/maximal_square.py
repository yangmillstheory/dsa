class Solution(object):
    def _brute_force(self, g):
        # T(m,n) = O((m*n)^2)
        # S(m,n) = O(1)
        m, n = len(g), len(g[0])
        best = 0
        for i in range(m):
            for j in range(n):
                add_dim = 0
                can_add = True
                while i+add_dim < m and j+add_dim < n and can_add:
                    # traverse a col
                    for k in range(i, i+add_dim+1):
                        if g[k][j+add_dim] != '1':
                            can_add = False
                            break
                    # traverse a row
                    for k in range(j, j+add_dim+1):
                        if g[i+add_dim][k] != '1':
                            can_add = False
                            break
                    add_dim += 1
                    if can_add:
                        best = max(best, pow(add_dim, 2))
        return best

    def _dp_1(self, g):
        # T(m, n) = O(m*n)
        # S(m, n) = O(m*n)
        m, n = len(g), len(g[0])
        dp = [[0]*n for _ in range(m)]
        best = 0
        for i in range(m):
            for j in range(n):
                if g[i][j] == '0':
                    continue
                dp[i][j] = min(
                    dp[i-1][j] if i-1 >= 0 else 0,
                    dp[i][j-1] if j-1 >= 0 else 0,
                    dp[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0,
                ) + 1
                best = max(best, pow(dp[i][j], 2))
        return best

    def _dp_2(self, g):
        # T(m, n) = O(m*n)
        # S(m, n) = O(n)
        m, n = len(g), len(g[0])
        prev = [0]*n
        curr = [0]*n
        best = 0
        for i in range(m):
            for j in range(n):
                if g[i][j] == '0':
                    curr[j] = 0
                else:
                    curr[j] = min(
                        curr[j-1] if j else 0,
                        prev[j-1] if j else 0,
                        prev[j],
                    ) + 1
                    best = max(best, pow(curr[j], 2))
            for j in range(n):
                prev[j] = curr[j]
        return best

    def _dp_3(self, g):
        # T(m, n) = O(m*n)
        # S(m, n) = O(n)
        m, n = len(g), len(g[0])
        dp = [0]*n
        best = 0
        prev = 0
        for i in range(m):
            for j in range(n):
                if g[i][j] == '0':
                    dp[j] = 0
                else:
                    temp = dp[j]
                    dp[j] = min(
                        dp[j-1] if j else 0,
                        dp[j],
                        prev,
                    ) + 1
                    best = max(best, pow(dp[j], 2))
                    prev = temp
        return best

    def maximalSquare(self, g):
        if not g or not g[0]:
            return 0
        return self._dp_3(g)
