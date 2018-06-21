class Solution(object):
    def _is_subseq_dp(self, pat, text):
        if not text:
            return True
        if not pat:
            return True
        t, p = len(text), len(pat)
        memo = [False]*p
        for i in range(t):
            for j in range(p-1, -1, -1):
                memo[j] = memo[j] or (
                        True if j-1 < 0 else memo[j-1] and
                        text[i] == pat[j])
        return memo[-1]

    def isSubsequence(self, pat, text):
        k = 0
        for ch in text:
            if ch == pat[k]:
                k += 1
            if k == len(pat):
                return True
        return False
