from collections import Counter


class Solution:
    def minWindow(self, text, pat):
        '''Find the minimum window covering a pattern possibly with
        duplicate tokens.

            T(t, p) = O(t)
            S(t, p) = O(p)
        '''
        n, j = len(text), 0
        orig = Counter(pat)
        have = Counter()
        rem = set(pat)
        pat = set(pat)
        sub = ''
        for i in range(n):
            if rem:
                # expand right to cover pat
                while j < n and rem:
                    ch = text[j]
                    if ch in pat:
                        have[ch] += 1
                    if have[ch] >= orig[ch] and ch in rem:
                        rem.remove(ch)
                    j += 1
            if not rem and (sub == '' or j-i < len(sub)):
                sub = text[i:j]
            ch = text[i]
            if ch in have:
                have[ch] -= 1
                if have[ch] < orig[ch]:
                    rem.add(ch)
        return sub


if __name__ == '__main__':
    s = Solution()
    assert s.minWindow('ab', 'b') == 'b'
    assert s.minWindow('aa', 'aa') == 'aa'
    assert s.minWindow('aabbbaaa', 'aaa') == 'aaa'
    assert s.minWindow('adobecodebanc', 'abc') == 'banc'
