class Solution(object):
    def maxArea(self, hs):
        # T(n) = O(n)
        lo, hi = 0, len(hs)-1
        _max_area = 0
        while lo <= hi:
            min_h, i = min([(hs[lo], lo), (hs[hi], hi)])
            _max_area = max(_max_area, (hi-lo)*min_h)
            if i == hi:
                hi -= 1
            else:
                lo += 1
        return _max_area
