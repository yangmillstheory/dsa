class Solution:
    def setZeroes(self, g):
        # T(m,n) = O(m*n)
        if not g or not g[0]:
            return
        m, n = len(g), len(g[0])
        row_0_marked, col_0_marked = True, True
        for j in range(n):
            if g[0][j] == 0:
                break
        else:
            row_0_marked = False
        for i in range(m):
            if g[i][0] == 0:
                break
        else:
            col_0_marked = False
        for i in range(1, m):
            for j in range(1, n):
                if g[i][j] == 0:
                    g[i][0] = 0
                    g[0][j] = 0
        for i in range(1, m):
            if g[i][0] == 0:
                for j in range(n):
                    g[i][j] = 0
        for j in range(1, n):
            if g[0][j] == 0:
                for i in range(m):
                    g[i][j] = 0
        if row_0_marked:
            for j in range(n):
                g[0][j] = 0
        if col_0_marked:
            for i in range(m):
                g[i][0] = 0


if __name__ == '__main__':
    g = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s = Solution()
    s.setZeroes(g)
    print(g)
    g = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(g)
    print(g)
