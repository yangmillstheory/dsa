class Solution(object):
    def findLengthOfLCIS(self, a):
        '''Return the length of the longest increasing subarray in O(n) time and O(1) space.'''
        best = curr = 0
        for i, x in enumerate(a):
            if i == 0 or x > a[i-1]:
                curr += 1
            else:
                curr = 1
            best = max(best, curr)
        return best
