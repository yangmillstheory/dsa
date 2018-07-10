import re


class Solution(object):
    def reverseWords(self, s):
        # sanitize
        s = re.sub(r'\s{2,}', ' ', s.strip())
        # reverse entire string, then reverse each word
        s = s[::-1]
        res, i, n = [], 0, len(s)
        for j in range(n+1):
            if j == n or s[j].isspace():
                if not i:
                    t = s[j-1::-1]
                else:
                    t = s[j-1:i:-1]
                res.append(t)
                i = j
        return ' '.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords('the sky is blue'))
