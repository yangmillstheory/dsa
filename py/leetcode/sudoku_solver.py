GRID_DIM = 9
EMPTY = '.'


def next_pos(i, j):
    j += 1
    if j == GRID_DIM:
        i += 1
        j = 0
    return i, j

class Solution:
    def _can_add(self, grid, i, j, x):
        if x in grid[i]:
            return False
        if x in [grid[l][j] for l in range(GRID_DIM)]:
            return False
        k, l = i-(i%3), j-(j%3)
        if x in [grid[p][q] for p in range(k, k+3) for q in range(l, l+3)]:
            return False
        return True

    def _solve(self, grid, i, j):
        if i == GRID_DIM:
            return True
        if grid[i][j] != EMPTY:
            return self._solve(grid, *next_pos(i, j))
        for k in range(1, GRID_DIM+1):
            k = str(k)
            if not self._can_add(grid, i, j, k):
                continue
            grid[i][j] = k
            if self._solve(grid, *next_pos(i, j)):
                return True
        grid[i][j] = EMPTY
        return False

    def solveSudoku(self, grid):
        self._solve(grid, 0, 0)
