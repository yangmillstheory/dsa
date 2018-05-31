class Solution:
    def minPathSum(self, grid):
        '''Minimum path sum in T(m, n) = O(m*n), S(m, n) = O(1),
        mutates grid to achieve O(1) space complexity.
        '''
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] = grid[i][0] + grid[i-1][0]
        for j in range(1, n):
            grid[0][j] = grid[0][j] + grid[0][j-1]
        for j in range(1, n):
            for i in range(1, m):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[m-1][n-1]
