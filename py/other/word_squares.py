from collections import defaultdict
from io import StringIO


class Trie:
    def __init__(self):
        self.links = defaultdict(self.__class__)
        self.words = set()
        self.is_word = False

    def insert(self, word):
        trie = self
        for ch in word:
            trie = trie.links[ch]
            trie.words.add(word)
        trie.is_word = True

    def search(self, prefix):
        trie = self
        for ch in prefix:
            if ch not in trie.links:
                return None
            trie = trie.links[ch]
        return trie


def word_squares(words):
    '''Find all valid word squares in O(n*k) time and O(n) space.'''
    res = []
    root = Trie()
    for word in words:
        root.insert(word)
    for word in words:
        _backtrack(root, len(word), [word], res)
    return res


def _backtrack(root, n, sq, res):
    if len(sq) == n:
        res.append(sq[:])
    else:
        j = len(sq)
        buf = StringIO()
        for i in range(j):
            buf.write(sq[i][j])
        prefix = buf.getvalue()
        trie = root.search(prefix)
        if trie:
            for word in trie.words:
                _backtrack(root, n, sq + [word], res)
    return res


if __name__ == '__main__':
    res = word_squares(['BALL', 'LEAD', 'AREA', 'LADY'])
    assert res == [
        [
            'BALL',
            'AREA',
            'LEAD',
            'LADY',
        ],
    ], res

    res = word_squares(['sator', 'arepo', 'tenet', 'opera', 'rotas'])
    assert res == [
        [
            'sator',
            'arepo',
            'tenet',
            'opera',
            'rotas',
        ],
        [
            'rotas',
            'opera',
            'tenet',
            'arepo',
            'sator',
        ]
    ], res
