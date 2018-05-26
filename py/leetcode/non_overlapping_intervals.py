from collections import namedtuple

Ival = namedtuple('Ival', ['start', 'end'])


class Solution:
    def eraseOverlapIntervals(self, ivals):
        if not ivals:
            return 0
        ivals.sort(key=lambda ival: (ival.start, ival.end))
        last_e = ivals[0].end
        n = 0
        for ival in ivals[1:]:
            if ival.end < last_e:
                # remove the containing interval
                n += 1
                last_e = ival.end
            elif ival.start < last_e:
                n += 1
            else:
                last_e = ival.end
        return n


if __name__ == '__main__':
    s = Solution()
    n = s.eraseOverlapIntervals([Ival(1,2), Ival(2,3), Ival(3,4), Ival(1,3)])
    assert n == 1, n

    n = s.eraseOverlapIntervals([Ival(1,2), Ival(1,2), Ival(1,2)])
    assert n == 2, n

    n = s.eraseOverlapIntervals([Ival(1,2), Ival(2, 3)])
    assert n == 0, n

    n = s.eraseOverlapIntervals([Ival(1,2), Ival(0, 3)])
    assert n == 1, n

    n = s.eraseOverlapIntervals([Ival(1, 4), Ival(2, 3), Ival(3, 6)])
    assert n == 1, n
