import string


class Solution(object):
    def detectCapitalUse(self, word):
        n = len(word)
        if not n:
            return True
        n_caps = 0
        for ch in word:
            if ch in string.ascii_uppercase:
                n_caps += 1
        return n_caps in (0, n) or (n_caps == 1 and word[0] in string.ascii_uppercase)
