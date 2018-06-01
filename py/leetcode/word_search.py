class Solution:
    def __init__(self):
        self.grid = None
        self.word = None

    def _exist(self, i, j, pos, seen):
        if self.grid[i][j] != self.word[pos]:
            return False
        if pos == len(self.word)-1:
            return True
        seen.add((i, j))
        m, n = len(self.grid), len(self.grid[0])
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if min(i+di, j+dj) < 0 or i+di >= m or j+dj >= n:
                continue
            elif (i+di, j+dj) in seen:
                continue
            if self._exist(i+di, j+dj, pos+1, seen):
                return True
        seen.remove((i, j))
        return False

    def exist(self, grid, word):
        '''Word search in T(m,n) = O(m*n*w) and S(n) = O(w).'''
        if not grid or not grid[0] or not word:
            return False
        self.grid = grid
        self.word = word
        m, n = len(self.grid), len(self.grid[0])
        seen = set()
        for i in range(m):
            for j in range(n):
                if self._exist(i, j, 0, seen):
                    return True
        return False
