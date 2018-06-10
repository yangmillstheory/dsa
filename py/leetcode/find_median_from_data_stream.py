import heapq


class MedianFinder(object):
    '''Finds the median of a stream of integers with S(n) = O(n).

    Adding an integer is T(n) = O(log n) and finding the median is T(n) = O(1).
    '''
    def __init__(self):
        # invariants:
        #
        #    1. max(self._lower) <= min(self._upper)
        #    2. abs(len(self._lower)-len(self._upper)) <= 1
        #
        self._upper = []  # min heap
        self._lower = []  # max heap

    def addNum(self, x):
        if self._lower and self._upper:
            if x > max(-self._lower[0], self._upper[0]):
                heapq.heappush(self._upper, x)
            elif x < min(-self._lower[0], self._upper[0]):
                heapq.heappush(self._lower, -x)
            else:
                # choose at random, we'll rebalance later
                heapq.heappush(self._lower, -x)
        elif not self._lower or (not self._upper and x < -self._lower[0]):
            heapq.heappush(self._lower, -x)
        else:
            heapq.heappush(self._upper, x)
        m, n = len(self._lower), len(self._upper)
        if m > n+1:
            heapq.heappush(self._upper, -heapq.heappop(self._lower))
        elif n > m+1:
            heapq.heappush(self._lower, -heapq.heappop(self._upper))

    def findMedian(self):
        m, n = len(self._lower), len(self._upper)
        if m > n:
            return -self._lower[0]
        elif m < n:
            return self._upper[0]
        elif not self._lower and not self._upper:
            return None
        return (-self._lower[0]+self._upper[0])/2.0
