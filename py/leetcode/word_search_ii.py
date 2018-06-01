from collections import defaultdict


VISITING = '*'


class Trie:
    def __init__(self):
        self.links = defaultdict(self.__class__)
        self.is_word = False

    def insert(self, word):
        trie = self
        for ch in word:
            trie = trie.links[ch]
        trie.is_word = True


class Solution:
    def findWords(self, grid, words):
        if not grid or not grid[0] or not words:
            return []
        res = set()
        root = Trie()
        for word in words:
            root.insert(word)

        m, n = len(grid), len(grid[0])

        def explore(i, j, trie, pre=''):
            '''Find words in the grid. Works as follows:

            1. Build a prefix tree of the set of words
            2. DFS on each cell of the grid; backtracking happens
               when the current path is not in the prefix tree; this
               avoids repeating the same bad path for words having
               the same prefix.
            3. During DFS, if a word in the prefix tree is found, add
               it to the set of words.
            '''
            ch = grid[i][j]
            if ch not in trie.links:
                return
            grid[i][j] = VISITING
            trie = trie.links[ch]
            pre += ch
            if trie.is_word:
                res.add(pre)
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj] != VISITING:
                    explore(i+di, j+dj, trie, pre)
            grid[i][j] = ch

        for i in range(m):
            for j in range(n):
                explore(i, j, root)
        return list(res)
