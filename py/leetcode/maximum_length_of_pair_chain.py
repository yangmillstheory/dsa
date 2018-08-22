import operator


class Solution(object):
    def findLongestChain(self, a):
        if not a:
            return 0
        a.sort(key=operator.itemgetter(1))
        curr, n = float('-inf'), 0
        for x, y in a:
            if curr < x:
                n += 1
                curr = y
        return n
