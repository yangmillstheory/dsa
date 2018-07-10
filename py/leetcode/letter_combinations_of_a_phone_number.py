keypad = {
    '0': '0',
    '1': '1',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution(object):
    def letterCombinations(self, s, i=0, cand=None, res=None):
        # T(n) = O(n*4^n)
        # S(n) = O(n)
        if res is None:
            res = []
        if not s:
            return res
        if cand is None:
            cand = []
        if i == len(s):
            res.append(''.join(cand))
        else:
            for ch in keypad[s[i]]:
                cand.append(ch)
                self.letterCombinations(s, i+1, cand, res)
                cand.pop()
        return res
