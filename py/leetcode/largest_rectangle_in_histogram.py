class Solution(object):
    def largestRectangleArea(self, a):
        stack, best = [], 0
        for i, h in enumerate(a + [0]):
            while stack and a[stack[-1]] > h:
                j = stack.pop()
                w = i-stack[-1]-1 if stack else i
                best = max(best, w*a[j])
            stack.append(i)
        return best
