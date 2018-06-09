import heapq


class Solution(object):
    def findClosestElements(self, xs, k, x):
        '''Find k closest elements in an array in O(n*log k) time and O(k) space.
        Ties are broken by element values.'''
        heap = []
        for z in xs:
            heapq.heappush(heap, (-abs(z-x), -z))
            if len(heap) == k+1:
                heapq.heappop(heap)
        return sorted([-t[1] for t in (heapq.heappop(heap) for _ in range(k))])
