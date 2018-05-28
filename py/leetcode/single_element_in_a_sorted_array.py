class Solution:
    def singleNonDuplicate(self, xs):
        n = len(xs)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = int(lo + (hi-lo)/2)
            if mid and xs[mid-1] == xs[mid]:
                if mid-2 >= lo and (mid-lo-1) % 2 != 0:
                    hi = mid-2
                else:
                    lo = mid+1
            elif mid+1 < n and xs[mid+1] == xs[mid]:
                if mid+2 <= hi and (hi-mid-1) % 2 != 0:
                    lo = mid+2
                else:
                    hi = mid-1
            else:
                return xs[mid]
        raise ValueError


if __name__ == '__main__':
    xs = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    assert Solution().singleNonDuplicate(xs) == 2

    xs = [3, 3, 7, 7, 10, 11, 11]
    assert Solution().singleNonDuplicate(xs) == 10

    xs = [1, 1, 2, 2, 4, 4, 5, 5, 9]
    assert Solution().singleNonDuplicate(xs) == 9
