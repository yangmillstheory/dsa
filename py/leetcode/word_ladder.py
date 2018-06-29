import collections


class Solution(object):
    def ladderLength(self, s, t, words):
        words.append(s)
        words = set(words)
        alpha = {ch for word in words for ch in word}
        q, seen = collections.deque([(s, 1)]), set()
        while q:
            v, n = q.popleft()
            if v == t:
                return n
            chars = list(v)
            for i, ch in enumerate(v):
                for _ch in alpha:  # only use characters for edges that come from words
                    chars[i] = _ch
                    u = ''.join(chars)
                    if u in words and u not in seen and u != v:
                        q.append((u, n+1))
                    seen.add(u)
                chars[i] = ch
            seen.add(v)
        return 0
