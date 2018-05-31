class Solution:
    def uniquePaths(self, m, n):
        # T(m,n) = O(m*n)
        # S(m,n) = O(1)
        memo = [1 for _ in range(n)]
        for _ in range(1, m):
            for j in range(1, n):
                memo[j] += memo[j-1]
        return memo[n-1]
