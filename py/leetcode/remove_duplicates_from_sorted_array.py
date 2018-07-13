class Solution(object):
    def removeDuplicates(self, a):
        '''Remove duplicates from a sorted array in place in O(n) time.'''
        i = w = 0
        n = len(a)
        while i < n:
            while i and i < n and a[i] == a[i-1]:
                i += 1
            if i == n:
                break
            a[w] = a[i]
            i += 1
            w += 1
        return w
