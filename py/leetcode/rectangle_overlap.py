class Solution(object):
    def isRectangleOverlap(self, r1, r2):
        if r1[0] > r2[0]:
            r1, r2 = r2, r1
        if r1[2] <= r2[0] or r1[3] <= r2[1]:
            return False
        return min(r1[1], r1[3]) < r2[3]
