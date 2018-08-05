class Solution(object):
    def pivotIndex(self, a):
        if not a:
            return -1
        n, lsum, _sum = len(a), 0, sum(a)
        for i in range(1, n):
            lsum += a[i-1]
            rsum = _sum - lsum - a[i]
            if lsum == rsum:
                return i
        return -1
