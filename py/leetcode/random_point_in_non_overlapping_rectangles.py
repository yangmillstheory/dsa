import bisect
import functools
import random


def area(x1, y1, x2, y2):
    return (x2-x1+1)*(y2-y1+1)


class Solution(object):
    def __init__(self, rects):
        self._rects = rects
        self._areas, s = [], 0
        for rect in self._rects:
            s += area(*rect)
            self._areas.append(s)

    def pick(self):
        x = random.uniform(0, self._areas[-1])
        j = bisect.bisect_left(self._areas, x)
        x1, y1, x2, y2 = self._rects[j]
        return [
            random.randint(x1, x2),
            random.randint(y1, y2),
        ]
