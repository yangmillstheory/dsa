import collections
import heapq
import io


class Solution:
    def frequencySort(self, string):
        '''Frequency sort in O(n*log n) time and O(n) space.'''
        if not string:
            return ''
        heap, hist = [], collections.Counter(string)
        for ch, freq in hist.items():
            heapq.heappush(heap, (-freq, ch))
        buf = io.StringIO()
        while heap:
            freq, ch = heapq.heappop(heap)
            freq = -freq
            for _ in range(freq):
                buf.write(ch)
        return buf.getvalue()
