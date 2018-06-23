class Solution(object):
    def _word_break(self, s, words, start, seen):
        if start == len(s):
            return True
        if start in seen:
            return False
        for i in range(start+1, len(s)+1):
            if i in seen:
                continue
            sub = s[start:i]
            if sub in words:
                if self._word_break(s, words, i, seen):
                    return True
        seen.add(start)
        return False

    def wordBreak(self, s, words):
        return self._word_break(s, set(words), 0, set())
