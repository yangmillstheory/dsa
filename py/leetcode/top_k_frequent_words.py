from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, words, k):
        '''Top k frequent words in O(n*log k) time and O(n) space.'''
        res = []
        if not words:
            return res
        heap = []
        for word, freq in Counter(words).items():
            heappush(heap, (-freq, word))
        return [heappop(heap)[1] for _ in range(k)]
