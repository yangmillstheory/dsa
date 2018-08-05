class Solution(object):
    def searchRange(self, a, q):
        def midpoint(x, y):
            return x+(y-x)//2
        lo, hi = 0, len(a)-1
        _max = -1
        _min = -1
        while lo <= hi:
            mid = midpoint(lo, hi)
            if a[mid] == q:
                _max = max(_max, mid)
                if _min == -1:
                    _min = mid
            if a[mid] <= q:
                lo = mid+1
            else:
                hi = mid-1
        if _max == -1:
            return [_min, _max]
        lo, hi = 0, _min
        while lo <= hi:
            mid = midpoint(lo, hi)
            if a[mid] == q:
                _min = min(_min, mid)
            if a[mid] >= q:
                hi = mid-1
            else:
                lo = mid+1
        return [_min, _max]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
