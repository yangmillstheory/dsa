from functools import total_ordering
from collections import Counter
from heapq import heappush, heappop


class Solution:
    class HeapItem(object):
        def __init__(self, freq, word):
            self.freq = freq
            self.word = word

        def __lt__(self, other):
            if self.freq == other.freq:
                return self.word > other.word
            return self.freq < other.freq

        def __eq__(self, other):
            return self.freq == other.freq and self.word == other.word

    def topKFrequent(self, words, k):
        '''Top k frequent words in O(n*log k) time and O(n) space.'''
        res = []
        if not words:
            return res
        heap = []
        for word, freq in Counter(words).items():
            heappush(heap, self.HeapItem(freq, word))
            if len(heap) > k:
                heappop(heap)
        return [heappop(heap).word for _ in range(k)][::-1]
