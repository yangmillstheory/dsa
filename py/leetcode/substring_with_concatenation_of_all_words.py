from collections import Counter


class Solution:
    def findSubstring(self, string, words):
        '''Find starting indices of substrings that are concatenations of words.

        T(n, w, W) = O(n*w*W)
        S(n, w, W) = O(w)
        '''
        res = []
        n_words = len(words)
        if not n_words:
            return res
        n_word = len(words[0])
        orig = set(words)
        n = len(string)
        bad = set()
        for i in range(n-(n_words*n_word)+1):
            if i in bad:
                continue
            rem = Counter(words)
            for j in range(i, n-n_word+1, n_word):
                sub = string[j:j+n_word]
                if sub not in orig:
                    bad.add(j)
                    break
                if sub in rem:
                    rem[sub] -= 1
                    if not rem[sub]:
                        del rem[sub]
                    if not rem:
                        res.append(i)
                        break
                else:
                    break
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.findSubstring('barfoothefoobarman', ['foo', 'bar']) == [0, 9]
    assert s.findSubstring('wordgoodstudentgoodword', ['word', 'student']) == []
    assert s.findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'good']) == [8]
