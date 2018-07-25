class Solution(object):
    def combinationSum2(self, a, q):
        n, res, cand = len(a), [], []
        a.sort()

        def backtrack(start=0, partial=0):
            if partial == q:
                res.append(cand[:])
            else:
                for j in range(start, n):
                    if partial+a[j] > q:
                        break
                    elif j > start and a[j] == a[j-1]:
                        continue
                    cand.append(a[j])
                    backtrack(j+1, partial+a[j])
                    cand.pop()
        backtrack()
        return res
