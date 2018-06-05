class Solution:
    def _swap(self, xs, i, j):
        xs[i], xs[j] = xs[j], xs[i]

    def _permute(self, xs, cand, res):
        # not really sure why this approach works and others don't...
        n = len(xs)
        if not n:
            res.append(cand[:])
        else:
            for j in range(n):
                if j and xs[j] == xs[j-1]:
                    continue
                cand.append(xs[j])
                self._permute(xs[:j] + xs[j+1:], cand, res)
                cand.pop()
        return res

    def permuteUnique(self, xs):
        xs.sort()
        return self._permute(xs, [], [])
