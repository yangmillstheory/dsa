class MagicDictionary(object):
    def buildDict(self, words):
        self._words = words

    def search(self, query):
        def is_one_away(s, t):
            if len(s) != len(t):
                return False
            n_diff = 0
            for ch_s, ch_t in zip(s, t):
                if ch_s != ch_t:
                    n_diff += 1
                if n_diff > 1:
                    return False
            return n_diff == 1
        for w in self._words:
            if is_one_away(w, query):
                return True
        return False
