from collections import namedtuple

Pillar = namedtuple('Pillar', ['i', 'h'])


class Solution(object):
    def largestRectangleArea(self, hs):
        pillars, res = [], 0
        for i, h in enumerate(hs + [0]):
            while pillars and pillars[-1].h > h:
                _i, _h = pillars.pop()
                w = i - pillars[-1].i - 1 if pillars else i
                res = max(res, w*_h)
            pillars.append(Pillar(i, h))
        return res
