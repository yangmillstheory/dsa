DELIMITER = ' '


def reverse(seq, lo, hi):
    while lo <= hi:
        seq[lo], seq[hi] = seq[hi], seq[lo]
        lo += 1
        hi -= 1


class Solution(object):
    def reverseWords(self, s):
        # do some cleanup
        s = s.strip()
        chars = []
        for i, ch in enumerate(s):
            if ch != DELIMITER or (i and s[i-1] != DELIMITER):
                chars.append(ch)
        # reverse entire string, then reverse each word
        n = len(chars)
        reverse(chars, 0, n-1)
        i = 0
        for j in range(n+1):
            if j == n or chars[j] == DELIMITER:
                reverse(chars, i, j-1)
                i = j+1
        return ''.join(chars)
