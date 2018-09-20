class Solution(object):
    def wordPattern(self, pattern, strings):
        # T(p, s) = O(min(p, s))
        # S(p, s) = O(max(p, s))
        pat_2_str = {}
        str_2_pat = {}
        strings = strings.split(' ')
        if len(strings) != len(pattern):
            return False
        for pat, string in zip(pattern, strings):
            if pat != str_2_pat.setdefault(string, pat):
                return False
            if string != pat_2_str.setdefault(pat, string):
                return False
        return True
