import bisect


class Solution(object):
    def findRadius(self, a, b):
        b.sort()
        n_heaters = len(b)
        radius = 0
        for h in a:
            i = bisect.bisect_left(b, h)
            if i == n_heaters or (i-1 >= 0 and abs(b[i-1]-h) <= abs(b[i]-h)):
                closer = b[i-1]
            else:
                closer = b[i]
            radius = max(radius, abs(h-closer))
        return radius
