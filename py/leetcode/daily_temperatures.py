class Solution(object):
    def dailyTemperatures(self, t):
        stack, n = [], len(t)
        res = [0]*n
        for i, x in enumerate(t):
            while stack and stack[-1][0] < x:
                _, j = stack.pop()
                res[j] = i-j
            stack.append((x, i))
        return res
