class Solution(object):
    def _unique_paths_dp(self, m, n):
        # T(m,n) = O(m*n)
        # S(m,n) = O(n)
        memo = [1 for _ in range(n)]
        for _ in range(1, m):
            for j in range(1, n):
                memo[j] += memo[j-1]
        return memo[n-1]

    def _unique_paths_recursive(self, m, n, cache):
        if min(m, n) <= 0:
            return 0
        if m == 1 or n == 1:
            return 1
        if (m, n) not in cache:
            cache[(m, n)] = self._unique_paths_recursive(m-1, n, cache) + self._unique_paths_recursive(m, n-1, cache)
        return cache[(m, n)]

    def uniquePaths(self, m, n):
        return self._unique_paths_recursive(m, n, {})
