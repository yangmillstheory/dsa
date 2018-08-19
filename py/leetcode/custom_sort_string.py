class Solution(object):
    def customSortString(self, s, t):
        ind = {ch: i for i, ch in enumerate(s)}

        def compare(p, q):
            ind_p = ind.get(p, float('+inf'))
            ind_q = ind.get(q, float('+inf'))
            if ind_p == ind_q:
                return 0
            return -1 if ind_p < ind_q else 1
        return ''.join(sorted(t, cmp=compare))
