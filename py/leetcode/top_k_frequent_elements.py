import collections
import heapq


class Solution:
    def topKFrequent(self, xs, k):
        '''k most frequent elements in O(n*log k) time and O(n) space.'''
        res = []
        if not xs:
            return res
        heap, hist = [], collections.Counter(xs)
        for x, count in hist.items():
            heapq.heappush(heap, (count, x))
            if len(heap) > k:
                heapq.heappop(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)][::-1]
