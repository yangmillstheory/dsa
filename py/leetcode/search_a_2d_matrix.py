from bisect import bisect_left


class Solution(object):
    def searchMatrix(self, g, x):
        '''T(n) = O(log n + log m) and S(n) = O(1)'''
        if not g or not g[0]:
            return False
        m, n = len(g), len(g[0])
        i = bisect_left([g[k][0] for k in range(m)], x)
        if i < m and g[i][0] == x:
            return True
        i = max(i-1, 0)
        j = bisect_left(g[i], x)
        return j < n and g[i][j] == x


if __name__ == '__main__':
    print(bisect_left([1, 2, 3], 1))
