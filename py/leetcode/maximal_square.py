class Solution(object):
    def _brute_force(self, grid):
        # T(m,n) = O((m*n)^2)
        # S(m,n) = O(1)
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        best = 0
        for i in range(m):
            for j in range(n):
                add_dim = 0
                can_continue = True
                while i+add_dim < m and j+add_dim < n and can_continue:
                    # traverse a col
                    for k in range(i, i+add_dim+1):
                        if grid[k][j+add_dim] != '1':
                            can_continue = False
                            break
                    # traverse a row
                    for k in range(j, j+add_dim+1):
                        if grid[i+add_dim][k] != '1':
                            can_continue = False
                            break
                    add_dim += 1
                    if can_continue:
                        best = max(best, pow(add_dim, 2))
        return best

    def maximalSquare(self, grid):
        return self._brute_force(grid)
