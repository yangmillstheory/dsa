from io import StringIO
from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(self.__class__)
        self.is_word = False

    def insert(self, word):
        node = self
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def get_shortest_prefix(self, word):
        # note that this returns word if no prefix is found
        pre = StringIO()
        node = self
        for ch in word:
            if node.is_word:
                break
            elif ch not in node.children:
                return word
            pre.write(ch)
            node = node.children[ch]
        else:
            if node.is_word:
                return pre.getvalue()
        return pre.getvalue()


class Solution:
    def _build_trie(self, dictionary):
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        return trie

    def replaceWords(self, dictionary, sentence):
        # T = max of number of words in dictionary/sentence + max length of a word from dictionary/sentence
        # S = sum of all the lengths of the words in the dictionary
        trie = self._build_trie(dictionary)
        return ' '.join([
            trie.get_shortest_prefix(word) for word in sentence.split(' ')])
