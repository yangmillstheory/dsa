class Solution(object):
    def dailyTemperatures(self, t):
        stack, n = [], len(t)
        res = [0]*n
        for i, x in enumerate(t):
            while stack and t[stack[-1]] < x:
                j = stack.pop()
                res[j] = i-j
            stack.append(i)
        return res
