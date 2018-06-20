class Solution(object):
    def _combination_sum(self, xs, q, subset, res, i):
        partial = sum(subset)
        if partial == q:
            res.append(subset[:])
        else:
            for j in range(i, len(xs)):
                if partial+xs[j] > q:
                    break
                subset.append(xs[j])
                self._combination_sum(xs, q, subset, res, j)
                subset.pop()
        return res

    def combinationSum(self, xs, q):
        xs.sort()
        return self._combination_sum(xs, q, [], [], 0)
