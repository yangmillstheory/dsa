GRID_DIM = 9


class Solution:
    def _check_valid_it(self, it):
        rem = set(range(1, 10))
        for x in it:
            if x == '.':
                continue
            x = int(x)
            if x not in rem:
                return False
            rem.remove(x)
        return True

    def isValidSudoku(self, grid):
        for row in grid:
            if not self._check_valid_it(row):
                return False
        for j in range(GRID_DIM):
            if not self._check_valid_it([grid[k][j] for k in range(GRID_DIM)]):
                return False
        for i in range(3):
            for j in range(3):
                subgrid = [
                    grid[k][l]
                    for k in range(3*i, (3*i)+3)
                    for l in range(3*j, (3*j)+3)
                ]
                if not self._check_valid_it(subgrid):
                    return False
        return True
