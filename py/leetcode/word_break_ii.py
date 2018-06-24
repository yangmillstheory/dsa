class Solution(object):
    def _word_break(self, s, words, start, seen, used, res):
        if start == len(s):
            res.append(' '.join(used[:]))
            return True
        if start in seen:
            return False
        found = False
        for i in range(start+1, len(s)+1):
            if i in seen:
                continue
            sub = s[start:i]
            if sub in words:
                used.append(sub)
                if self._word_break(s, words, i, seen, used, res):
                    found = True
                used.pop()
        if not found:
            seen.add(start)
        return found

    def wordBreak(self, s, words):
        res = []
        self._word_break(s, set(words), 0, set(), [], res)
        return res
