def ch_index(ch):
    return ord(ch)-ord('a')


class Solution(object):
    def canConstruct(self, note, magazine):
        '''O(1) space and O(max(m, n)) time solution for constructibility of a ransom note.'''
        if not note:
            return True
        chars = [0 for _ in range(ord('a'), ord('z')+1)]
        for ch in note:
            chars[ch_index(ch)] += 1
        remaining = sum(chars)
        for ch in magazine:
            j = ch_index(ch)
            if chars[j] > 0:
                chars[j], remaining = chars[j]-1, remaining-1
            if not remaining:
                return True
        return False
