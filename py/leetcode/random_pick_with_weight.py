from random import uniform
from bisect import bisect_left


class Solution:

    def __init__(self, weights):
        self._weights = weights
        self._ranges, s = [], 0
        for w in self._weights:
            s += w
            self._ranges.append(s)

    def pickIndex(self):
        x = uniform(0, self._ranges[-1])
        return bisect_left(self._ranges, x)
