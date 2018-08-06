class Solution(object):
    def rotate(self, a, k):
        '''Rotate an array in O(n) time and O(1) space.'''
        n = len(a)
        k %= n
        i = t = 0
        while i < k and t < n:
            prev = a[i]
            j = (i+k) % n
            while t < n:
                temp = a[j]
                a[j], prev = prev, temp
                t += 1
                if j == i:
                    # need this here instead of the loop
                    # condition since we want to swap into i
                    break
                j = (j+k) % n
            i += 1
