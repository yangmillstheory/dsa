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
