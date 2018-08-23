from collections import Counter


class Solution:
    def minWindow(self, text, pat):
        '''Find the minimum window covering a pattern possibly with
        duplicate tokens.

            T(t, p) = O(t)
            S(t, p) = O(p)
        '''
        n = len(text)
        j = 0
        orig = Counter(pat)
        have = Counter()
        rem = set(pat)
        sub = ''
        for i in range(n):
            while rem and j < n:
                # expand right to cover pat
                ch = text[j]
                if ch in orig:
                    have[ch] += 1
                    if have[ch] >= orig[ch] and ch in rem:
                        rem.remove(ch)
                j += 1
            if rem and j == n:
                break
            if not rem and ((not sub) or j-i < len(sub)):
                sub = text[i:j]
            ch = text[i]
            have[ch] -= 1
            if ch in orig and have[ch] < orig[ch]:
                rem.add(ch)
        return sub


if __name__ == '__main__':
    s = Solution()
    assert s.minWindow('ab', 'b') == 'b'
    assert s.minWindow('aa', 'aa') == 'aa'
    assert s.minWindow('aabbbaaa', 'aaa') == 'aaa'
    assert s.minWindow('adobecodebanc', 'abc') == 'banc'
