import bisect


class Solution(object):
    def findRadius(self, a, b):
        a.sort()
        b.sort()
        n_b = len(b)
        radius = 0
        for h in a:
            i = bisect.bisect_left(b, h)
            if i == n_b:
                closest = b[i-1]
            elif i-1 >= 0 and abs(b[i-1]-h) <= abs(b[i]-h):
                closest = b[i-1]
            else:
                closest = b[i]
            radius = max(radius, abs(h-closest))
        return radius
