import collections


class Solution:
    def firstUniqChar(self, string):
        hist = collections.Counter(string)
        for i, ch in enumerate(string):
            if hist[ch] == 1:
                return i
        return -1
