class Solution:
    def totalNQueens(self, n):
        res = {'n': 0}
        for i in range(n):
            self._n_queens(n, [i], res)
        return res['n']

    def _n_queens(self, n, cols, res):
        m = len(cols)
        if m == n:
            res['n'] += 1
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
