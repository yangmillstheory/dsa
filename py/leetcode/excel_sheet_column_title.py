from collections import deque


n_chars = ord('Z')-ord('A')+1


class Solution(object):
    def convertToTitle(self, n):
        '''Returns spreadsheet column title in O(n/n_chars) time and space.'''
        buf = deque()
        while n:
            n, rem = divmod(n-1, n_chars)
            buf.appendleft(chr(ord('A') + rem))
        return ''.join(buf)
