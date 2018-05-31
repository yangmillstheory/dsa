class Solution:
    def numIslands(self, grid):
        '''Count the number of islands in O(n) time and O(m*n)
        space. Mutates grid to save memory.
        '''
        n_islands = 0
        if not grid or not grid[0]:
            return n_islands
        m, n = len(grid), len(grid[0])
        visited = 'visited'

        def visit(i, j):
            grid[i][j] = visited
            adjacent = [
                (i+di, j+dj) for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1))
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj] == '1'
            ]
            for x, y in adjacent:
                if grid[x][y] != visited:
                    visit(x, y)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    visit(i, j)
                    n_islands += 1
        return n_islands
