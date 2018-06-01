from collections import defaultdict


def to_bits(x):
    return format(x, 'b').zfill(32)


class Trie:
    def __init__(self):
        self.links = defaultdict(self.__class__)
        self.x = None

    def insert(self, x):
        trie = self
        for bit in to_bits(x):
            trie = trie.links[bit]
        trie.x = x


class Solution:
    def findMaximumXOR(self, xs):
        best = float('-inf')
        root = Trie()
        for x in xs:
            root.insert(x)
        for x in xs:
            trie = root
            for bit in to_bits(x):
                # greedy choice
                if bit == '1' and '0' in trie.links:
                    trie = trie.links['0']
                elif bit == '0' and '1' in trie.links:
                    trie = trie.links['1']
                else:
                    trie = trie.links[bit]
            best = max(best, trie.x ^ x)
        return best
