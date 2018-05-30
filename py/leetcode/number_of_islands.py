class Solution:
    def numIslands(self, grid):
        '''Count the number of islands in O(n) time and O(m*n) space.'''
        n_islands = 0
        if not grid or not grid[0]:
            return n_islands
        m, n = len(grid), len(grid[0])
        # make sure to write this out to avoid all rows
        # referring to the same one:
        #
        #   https://stackoverflow.com/q/240178/2419669
        visited = [
            [False for _ in range(n)]
            for _ in range(m)
        ]

        def visit(i, j):
            visited[i][j] = True
            # adjacent land in the grid
            adjacent = [
                (i+di, j+dj) for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1))
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj] == '1'
            ]
            for x, y in adjacent:
                if visited[x][y]:
                    # note that we have to check this here and not the list
                    # comprehension since it may be mutated by recursive calls
                    continue
                visit(x, y)
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if grid[i][j] == '1':
                    visit(i, j)
                    n_islands += 1
        return n_islands
