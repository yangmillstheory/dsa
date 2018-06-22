VISITING = object()


class Solution:
    def __init__(self):
        self.grid = None
        self.word = None
        self.seen = None

    def _exist(self, i, j, pos):
        if (i, j, pos) in self.bad:
            return False
        if self.grid[i][j] != self.word[pos]:
            self.bad.add((i, j, pos))
            return False
        if pos == len(self.word)-1:
            return True
        m, n = len(self.grid), len(self.grid[0])
        t, self.grid[i][j] = self.grid[i][j], VISITING
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if min(i+di, j+dj) < 0 or i+di >= m or j+dj >= n:
                continue
            elif self.grid[i+di][j+dj] == VISITING or (i+di, j+dj, pos+1) in self.bad:
                continue
            if self._exist(i+di, j+dj, pos+1):
                return True
        self.grid[i][j] = t
        return False

    def exist(self, grid, word):
        '''Word search in T(m,n) = O(m*n*w) and S(n) = O(m*n*w).'''
        if not grid or not grid[0] or not word:
            return False
        self.grid = grid
        self.word = word
        self.bad = set()
        m, n = len(self.grid), len(self.grid[0])
        for i in range(m):
            for j in range(n):
                if self._exist(i, j, 0):
                    return True
        return False
