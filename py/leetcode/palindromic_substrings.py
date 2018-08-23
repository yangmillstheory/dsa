class Solution(object):
    def countSubstrings(self, string):
        n = len(string)
        c = 0
        for i in range(n):
            k = 0
            while i+k < n and i-k >= 0 and string[i-k] == string[i+k]:
                c += 1
                k += 1
            k = 0
            while i+1+k < n and i-k >= 0 and string[i-k] == string[i+1+k]:
                c += 1
                k += 1
        return c
