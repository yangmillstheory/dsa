class Solution(object):
    def _log_time_sq_root(self, k):
        lo, hi = 0, k
        cand = 0
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if pow(mid, 2) <= k:
                cand, lo = mid, mid+1
            else:
                hi = mid-1
        return cand

    def mySqrt(self, k):
        # return _linear_time_sq_root(k)
        return self._log_time_sq_root(k)
