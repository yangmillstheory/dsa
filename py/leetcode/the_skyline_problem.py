import collections
import heapq
import operator


class Solution(object):
    MaxHeapItem = collections.namedtuple('MaxHeapItem', ['neg_h', 'right'])

    def getSkyline(self, a):
        # T(n) = O(n*log(n))
        # S(n) = O(n)
        max_heap, skyline, i, n = [], [], 0, len(a)
        points = sorted(
            map(operator.itemgetter(0), a) +
            map(operator.itemgetter(1), a)
        )
        for p in points:
            while max_heap and max_heap[0].right <= p:
                heapq.heappop(max_heap)
            while i < n and a[i][0] == p:
                heapq.heappush(max_heap, self.MaxHeapItem(-a[i][2], a[i][1]))
                i += 1
            h = -max_heap[0].neg_h if max_heap else 0
            if not skyline or skyline[-1][1] != h:
                skyline.append([p, h])
        return skyline
