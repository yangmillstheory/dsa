class Solution(object):
    def _dp(self, s, words):
        # T(n) = O(n^3)
        # S(n) = O(n)
        n = len(s)
        dp = [True] + ([False]*n)
        for j in range(1, n+1):
            dp[j] = any(dp[i] and s[i:j] in words for i in range(j))
        return dp[-1]

    def _word_break(self, s, words, start, seen):
        if start == len(s):
            return True
        if start in seen:
            return False
        for i in range(start+1, len(s)+1):
            if i in seen:
                continue
            sub = s[start:i]
            if sub in words and self._word_break(s, words, i, seen):
                return True
        seen.add(start)
        return False

    def wordBreak(self, s, words):
        return self._dp(s, words)
