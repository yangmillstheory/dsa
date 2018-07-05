class Solution(object):
    def search(self, a, k):
        lo, hi = 0, len(a)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if a[mid] == k:
                return mid
            elif a[mid] > k:
                if a[mid] >= a[lo]:  # left half is sorted
                    if k >= a[lo]:
                        hi = mid-1
                    else:
                        lo = mid+1
                else:  # right half is sorted
                    hi = mid-1
            else:
                if a[mid] <= a[hi]:  # right half is sorted
                    if k <= a[hi]:
                        lo = mid+1
                    else:
                        hi = mid-1
                else:  # left half is sorted
                    lo = mid+1
        return -1
