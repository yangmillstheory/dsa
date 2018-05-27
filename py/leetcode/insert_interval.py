# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return '(%d, %d)' % (self.start, self.end)


def intersects(p, q):
    return not (p.end < q.start or q.end < p.start)


class Solution:
    def insert(self, ivals, new):
        if not ivals:
            return [new]
        res = []
        j, n = 0, len(ivals)
        while j < n and ivals[j].end < new.start:
            res.append(ivals[j])
            j += 1
        merged = new
        while j < n and intersects(merged, ivals[j]):
            merged.start = min(merged.start, ivals[j].start)
            merged.end = max(merged.end, ivals[j].end)
            j += 1
        res.append(merged)
        while j < n:
            res.append(ivals[j])
            j += 1
        return res


if __name__ == '__main__':
    s = Solution()

    ivals = [Interval(1, 3), Interval(6, 9)]
    res = s.insert(ivals, Interval(2, 5))
    assert res == [Interval(1, 5), Interval(6, 9)], res

    ivals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
    res = s.insert(ivals, Interval(4, 8))
    assert res == [Interval(1, 2), Interval(3, 10), Interval(12, 16)], res
