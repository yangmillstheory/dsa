from bisect import bisect_left


class Solution(object):
    def searchMatrix(self, g, x):
        '''T(m, n) = O(m * log n) and S(m, n) = O(1)'''
        if not g or not g[0]:
            return False
        for row in g:
            j = bisect_left(row, x)
            if j < len(row) and row[j] == x:
                return True
        return False

    def searchMatrix2(self, g, x):
        # note that this works for https://leetcode.com/problems/search-a-2d-matrix
        # but is slower than two binary searches; here, it's faster than the above.
        if not g or not g[0]:
            return False
        m, n = len(g), len(g[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if g[i][j] == x:
                return True
            if g[i][j] < x:
                i += 1
            else:
                j -= 1
        return False
