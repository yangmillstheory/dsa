class Solution(object):
    def decodeString(self, s):
        buf_n, buf_s = [], []
        n = 0
        for ch in s:
            if ch.isdigit():
                n = 10*n + int(ch)
            elif ch == '[':
                buf_n.append(n)
                n = 0
            elif ch == ']':
                buf = []
                while buf_s and buf_s[-1] != '[':
                    buf.append(buf_s.pop())
                if buf_s:
                    buf_s.pop()
                m = buf_n.pop() if buf_n else 1
                buf_s.append(m * ''.join(reversed(buf)))
            if ch.isalpha() or ch == '[':
                buf_s.append(ch)
        return ''.join(buf_s)
