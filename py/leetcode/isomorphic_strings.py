class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s_to_t = {}
        mapped = set()
        for i, ch in enumerate(s):
            if t[i] in mapped and ch not in s_to_t:
                # t[i] has more than one preimage
                return False
            mapped.add(s_to_t.setdefault(ch, t[i]))
            if s_to_t[ch] != t[i]:
                return False
        return True
