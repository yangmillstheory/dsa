import operator


def first_larger(intervals, lo, hi, q):
    first = -1
    while lo <= hi:
        mid = lo+(hi-lo)//2
        if intervals[mid].start >= q:
            first = mid
            hi = mid-1
        else:
            lo = mid+1
    return first


class Solution(object):
    def findRightInterval(self, intervals):
        # T(n) = O(n*log(n))
        # S(n) = O(n)
        n, ind = len(intervals), {interval: i for i, interval in enumerate(intervals)}
        intervals.sort(key=operator.attrgetter('start'))
        res = [-1]*n
        for i, interval in enumerate(intervals):
            j = first_larger(intervals, i+1, n-1, interval.end)
            if j != -1:
                res[ind[interval]] = ind[intervals[j]]
        return res
