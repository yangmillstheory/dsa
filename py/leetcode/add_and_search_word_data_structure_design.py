from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.links = defaultdict(self.__class__)
        self.is_word = False

    def addWord(self, word):
        node = self
        for ch in word:
            node = node.links[ch]
        node.is_word = True

    def search(self, pat, i=0):
        '''Search for a pattern in O(n) time where n is the size of the trie,
        and O(h) space where h is the height of the trie.'''
        if i == len(pat):
            return self.is_word
        ch = pat[i]
        if ch == '.':
            return any([child.search(pat, i+1) for child in self.links.values()])
        return ch in self.links and self.links[ch].search(pat, i+1)


if __name__ == '__main__':
    wd = WordDictionary()
    wd.addWord('bat')
    assert not wd.search('.')
    assert wd.search('b.t')
    assert wd.search('bat')
