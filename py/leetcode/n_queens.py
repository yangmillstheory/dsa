class Solution:
    def solveNQueens(self, n):
        res = []
        for i in range(n):
            self._n_queens(n, [i], res)
        return res

    def _n_queens(self, n, cols, res):
        m = len(cols)
        if m == n:
            res.append(self._make_grid(cols, n))
        else:
            for j in range(n):
                for row, col in enumerate(cols):
                    if abs(col-j) == m-row or j == col:
                        break
                else:
                    cols.append(j)
                    self._n_queens(n, cols, res)
                    cols.pop()
        return res

    def _make_grid(self, cols, n):
        return [
            ''.join([
                'Q' if j == col else '.' for j in range(n)])
            for col in cols
        ]
