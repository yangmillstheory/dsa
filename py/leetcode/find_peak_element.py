class Solution(object):
    def findPeakElement(self, xs):
        n = len(xs)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if mid-1 >= 0 and xs[mid] < xs[mid-1]:
                hi = mid-1
            elif mid+1 < n and xs[mid] < xs[mid+1]:
                lo = mid+1
            else:
                return mid
        raise Exception('wtf?')
