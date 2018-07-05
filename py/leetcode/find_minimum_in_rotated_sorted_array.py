class Solution(object):
    def findMin(self, a):
        # T(n) = O(log n)
        # S(n) = O(1)
        lo, hi = 0, len(a)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if a[mid] > a[hi]:
                lo = mid+1
            elif mid == 0 or (mid-1 >= 0 and a[mid-1] > a[mid]):
                return a[mid]
            else:
                hi = mid-1
        raise RuntimeError
