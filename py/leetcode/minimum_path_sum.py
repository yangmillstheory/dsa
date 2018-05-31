class Solution:
    def minPathSum(self, grid):
        '''Minimum path sum in T(m, n) = S(m, n) = O(m*n).'''
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        memo = [[None for _ in range(n)] for _ in range(m)]
        memo[0][0] = grid[0][0]
        for i in range(1, m):
            memo[i][0] = grid[i][0] + memo[i-1][0]
        for j in range(1, n):
            memo[0][j] = grid[0][j] + memo[0][j-1]
        for j in range(1, n):
            for i in range(1, m):
                memo[i][j] = min(memo[i-1][j], memo[i][j-1]) + grid[i][j]
        return memo[m-1][n-1]
