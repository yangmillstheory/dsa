class Solution(object):
    def longestPalindrome(self, string):
        best, n = '', len(string)
        s = f = 0
        for i in range(n):
            k = 0
            while i+k < n and i-k >= 0 and string[i-k] == string[i+k]:
                if f-s < 2*k + 1:
                    s, f = i-k, i+k+1
                k += 1
            k = 0
            while i+1+k < n and i-k >= 0 and string[i-k] == string[i+1+k]:
                if f-s < 2*(k+1):
                    s, f = i-k, i+k+2
                k += 1
        return best[s:f]
