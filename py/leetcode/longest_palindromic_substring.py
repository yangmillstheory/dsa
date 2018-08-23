class Solution(object):
    def longestPalindrome(self, s):
        best, n = '', len(s)
        for i in range(n):
            k = 0
            while i+k < n and i-k >= 0 and s[i-k] == s[i+k]:
                if len(best) < 2*k + 1:
                    best = s[i-k:i+k+1]
                k += 1
            k = 0
            while i+1+k < n and i-k >= 0 and s[i-k] == s[i+1+k]:
                if len(best) < 2*(k+1):
                    best = s[i-k:i+k+2]
                k += 1
        return best
