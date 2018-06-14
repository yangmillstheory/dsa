class Solution:
    # T(n) = O(n^2)
    def shortestPalindromeSlow(self, word):
        n = len(word)
        if not n:
            return ''
        pre = ''
        for j in reversed(range(n)):
            b = 0
            for i in reversed(range(j+1)):
                if i == b or word[i] != word[b]:
                    break
                b += 1
            if i <= b:
                break
            if i > b:
                pre += word[j]
        return pre+word

    # T(n) = O(n)
    # S(n) = O(1)
    def shortestPalindrome(self, word):
        n = len(word)
        if not n:
            return ''
        rev, i = word[::-1], 0
        for j in range(1, n+1):
            if rev[-j:] == word[:j]:
                i = j
        return rev[:n-i]+word
