class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start \
            and self.end == other.end


class Solution:
    def merge(self, ivals):
        res = []
        if not ivals:
            return res
        ivals.sort(key=lambda ival: (ival.start, ival.end))
        last = ivals[0]
        for ival in ivals[1:]:
            if ival.start <= last.end:
                last.end = max(ival.end, last.end)
            else:
                res.append(last)
                last = ival
        res.append(last)
        return res


if __name__ == '__main__':
    s = Solution()

    ivals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    res = s.merge(ivals)
    assert res == [Interval(1, 6), Interval(8, 10), Interval(15, 18)]

    ivals = [Interval(1, 4), Interval(4, 5)]
    res = s.merge(ivals)
    assert res == [Interval(1, 5)]
