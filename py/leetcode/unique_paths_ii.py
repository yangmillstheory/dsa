class Solution:
    def uniquePathsWithObstacles(self, grid):
        '''Count unique paths in a grid with obstacles in T(m,n) = O(m*n) and S(n) = O(1).'''
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        for j in range(n):
            if grid[0][j] == 1 or (j and grid[0][j-1] == 0):
                grid[0][j] = 0
            else:
                grid[0][j] = 1
        for i in range(1, m):
            if grid[i][0] == 1 or grid[i-1][0] == 0:
                grid[i][0] = 0
            else:
                grid[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]
